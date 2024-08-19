def execute_from_command_line(argv=None):
    utility = ManagmentUtility(argv)
    utility.execute()

def execute_from_input_stream(_command=None):
    utility = ManagmentUtility()
    utility.run_from_input_stream(_command)
    utility.execute()

import functools
import os
import pkgutil
import sys
import logging
from argparse import (
    _AppendConstAction,
    _CountAction,
    _StoreConstAction,
    _SubParsersAction,
)
from collections import defaultdict
from importlib import import_module

from core.management.base import BaseCommand, CommandError, CommandParser

def load_command_class(app_name, name):
    module = import_module("%score.management.commands.%s" % (app_name, name))
    return module.Command()

def find_commands(management_dir):
    command_dir = os.path.join(management_dir, "commands")
    return [
        name
        for _, name, is_pkg in pkgutil.iter_modules([command_dir])
        if not is_pkg and not name.startswith("_")
    ]

@functools.cache
def get_commands():
    commands = {name: "" for name in find_commands(os.path.dirname(__file__))}
    return commands


def call_command(command_name, *args, **options):
    """
    Call the given command, with the given options and args/kwargs.

    This is the primary API you should use for calling specific commands.

    `command_name` may be a string or a command object. Using a string is
    preferred unless the command object is required for further processing or
    testing.

    Some examples:
        call_command('migrate')
        call_command('shell', plain=True)
        call_command('sqlmigrate', 'myapp')

        from django.core.management.commands import flush
        cmd = flush.Command()
        call_command(cmd, verbosity=0, interactive=False)
        # Do something with cmd ...
    """
    if isinstance(command_name, BaseCommand):
        # Command object passed in.
        command = command_name
        command_name = command.__class__.__module__.split(".")[-1]
    else:
        # Load the command object by name.
        try:
            app_name = get_commands()[command_name]
        except KeyError:
            # raise CommandError("Unknown command: %r" % command_name)
            logging.warning("Unknown command: %r" % command_name)

        if isinstance(app_name, BaseCommand):
            # If the command is already loaded, use it directly.
            command = app_name
        else:
            command = load_command_class(app_name, command_name)

    # Simulate argument parsing to get the option defaults (see #10080 for details).
    parser = command.create_parser("", command_name)
    # Use the `dest` option name from the parser option
    opt_mapping = {
        min(s_opt.option_strings).lstrip("-").replace("-", "_"): s_opt.dest
        for s_opt in parser._actions
        if s_opt.option_strings
    }
    arg_options = {opt_mapping.get(key, key): value for key, value in options.items()}
    parse_args = []
    for arg in args:
        if isinstance(arg, (list, tuple)):
            parse_args += map(str, arg)
        else:
            parse_args.append(str(arg))

    def get_actions(parser):
        # Parser actions and actions from sub-parser choices.
        for opt in parser._actions:
            if isinstance(opt, _SubParsersAction):
                for sub_opt in opt.choices.values():
                    yield from get_actions(sub_opt)
            else:
                yield opt

    parser_actions = list(get_actions(parser))
    mutually_exclusive_required_options = {
        opt
        for group in parser._mutually_exclusive_groups
        for opt in group._group_actions
        if group.required
    }
    # Any required arguments which are passed in via **options must be passed
    # to parse_args().
    for opt in parser_actions:
        if opt.dest in options and (
            opt.required or opt in mutually_exclusive_required_options
        ):
            opt_dest_count = sum(v == opt.dest for v in opt_mapping.values())
            if opt_dest_count > 1:
                raise TypeError(
                    f"Cannot pass the dest {opt.dest!r} that matches multiple "
                    f"arguments via **options."
                )
            parse_args.append(min(opt.option_strings))
            if isinstance(opt, (_AppendConstAction, _CountAction, _StoreConstAction)):
                continue
            value = arg_options[opt.dest]
            if isinstance(value, (list, tuple)):
                parse_args += map(str, value)
            else:
                parse_args.append(str(value))
    defaults = parser.parse_args(args=parse_args)
    defaults = dict(defaults._get_kwargs(), **arg_options)
    # Raise an error if any unknown options were passed.
    stealth_options = set(command.base_stealth_options + command.stealth_options)
    dest_parameters = {action.dest for action in parser_actions}
    valid_options = (dest_parameters | stealth_options).union(opt_mapping)
    unknown_options = set(options) - valid_options
    if unknown_options:
        raise TypeError(
            "Unknown option(s) for %s command: %s. "
            "Valid options are: %s."
            % (
                command_name,
                ", ".join(sorted(unknown_options)),
                ", ".join(sorted(valid_options)),
            )
        )
    # Move positional args out of options to mimic legacy optparse
    args = defaults.pop("args", ())
    if "skip_checks" not in options:
        defaults["skip_checks"] = True

    return command.execute(*args, **defaults) 


import sys, os
from collections import defaultdict

class ManagmentUtility:
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        if self.prog_name == "__main__.py":
            self.prog_name = "python -m django"
        self.settings_exception = None

    def run_from_input_stream(self, _command:str=None):
        self.argv = ['main.py'] + _command.split()

    def main_help_text(self, commands_only=False):
        if commands_only:
            usage = sorted(get_commands())
        else:
            usage = [
                "",
                "Type '%s help <subcommand>' for help on a specific subcommand."
                % self.prog_name,
                "",
                "Available subcommands:",
            ]
            command_dict= defaultdict(lambda: [])
            for name, app in get_commands().items():
                match app:
                    case 'django.core': app = 'django'
                    case _: app = app.rpartition(".")[-1]
                command_dict[app].append(name)
            # style = color_style()

            for app in sorted(command_dict):
                usage.append("")
                # usage.append(style.NOTICE("[%s]" % app))
                for name in sorted(command_dict[app]):
                    usage.append("    %s" % name)

        # if self.settings_exception:
        #     usage.append(
        #         style.NOTICE(
        #             "Note that only Django core commands are listed "
        #             "as settings are not properly configured (error: %s)."
        #             % self.settings_exception
        #         )
        #     )

        return "\n".join(usage)
    
    def fetch_commands(self, subcommand):
        commands = get_commands()
        try:
            app_name = commands[subcommand]
        except KeyError:
            app_name = commands['unknown_command']
            subcommand = 'unknown_command'

        if isinstance(app_name, BaseCommand):
            # If the command is already loaded, use it directly.
            klass = app_name
        else:
            klass = load_command_class(app_name, subcommand)
        return klass



    def execute(self):
        try: subcommand = self.argv[1]
        except IndexError: subcommand = 'help'

        parser = CommandParser(
            prog = self.prog_name,
            usage="%(prog)s subcommand [options] [args]",
            add_help=False,
            allow_abbrev=False,
        )
        parser.add_argument('--settings')
        parser.add_argument('--pythonpath')
        parser.add_argument('args', nargs="*")

        try:
            options, args = parser.parse_known_args(self.argv[2:])
            # handle_defaul_options(options)\
        except CommandError:pass

        # self.autocomplete()
        
        match subcommand:
            case "-v" | "--version":
                sys.stdout.write('0.0' + "\n")
            
            case '--help' | '-h' | 'help':
                sys.stdout.write(self.main_help_text() + "\n")
            case 'exit' | 'quit':
                sys.exit(0)
            case _: 
                self.fetch_commands(subcommand).run_from_argv(self.argv)

