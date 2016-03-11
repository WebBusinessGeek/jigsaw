#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import click
import strings

click.BaseCommand.ignore_unknown_options = True
click.BaseCommand.allow_extra_args = True


def _flatten_list_of_lists(l):
    return [item for sublist in l for item in sublist]


def _normalize_answer(choices, selection):
    for i in xrange(len(choices)):
        if selection in choices[i]:
            return choices[i][2]


def _make_choice_list(choices):
    indices = [str(i + 1) for i in xrange(len(choices))]
    return map((lambda curr_choice, index: [
        index,
        "({}) {}".format(index, curr_choice),
        curr_choice,
    ]), choices, indices)


# TODO refactor all this setup code below

project_type_choices = _make_choice_list([
    strings.RESTFUL,
    strings.WEB_APP,
    strings.BOTH_RESTFUL_AND_WEB_APP,
])

framework_lang_choices = _make_choice_list([
    strings.JAVA_UNDERTOW,
    strings.ECMASCRIPT_EXPRESS,
    strings.SCALA_AKKA,
])

CHOOSE_API_FRAMEWORK_PROMPT = "{}{}".format(strings.CHOOSE_API_FRAMEWORK_PROMPT_BASE, '\n')
for choice in framework_lang_choices:
    CHOOSE_API_FRAMEWORK_PROMPT += choice[1] + '\n'

RESTFUL_AND_OR_WEB_APP_PROMPT = "{}{}".format(strings.RESTFUL_AND_OR_WEB_APP_PROMPT_BASE, '\n')
for choice in project_type_choices:
    RESTFUL_AND_OR_WEB_APP_PROMPT += choice[1] + '\n'


@click.command()
@click.option('--project-type',
              type=click.Choice(_flatten_list_of_lists(project_type_choices)),
              prompt=RESTFUL_AND_OR_WEB_APP_PROMPT)
def jigsaw(project_type):
    project_type = _normalize_answer(project_type_choices, project_type)

    click.echo("You chose: {}".format(project_type))

    print
    if project_type == strings.RESTFUL or project_type == strings.BOTH_RESTFUL_AND_WEB_APP:
        # do RESTful project setup
        # ctx.invoke(setup_restful_api)
        setup_restful_api()
        pass
    if project_type == strings.WEB_APP or project_type == strings.BOTH_RESTFUL_AND_WEB_APP:
        # do web app project setup
        # TODO add click command for web app projects
        pass


@click.command()
@click.option('--framework-and-lang',
              type=click.Choice(_flatten_list_of_lists(framework_lang_choices)),
              prompt=CHOOSE_API_FRAMEWORK_PROMPT)
def setup_restful_api(framework_and_lang):
    framework_and_lang = _normalize_answer(framework_lang_choices, framework_and_lang)

    click.echo("Setting up {}".format(framework_and_lang))
    print

    # TODO finish


if __name__ == '__main__':
    jigsaw()
