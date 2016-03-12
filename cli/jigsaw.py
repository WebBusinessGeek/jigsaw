#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import click
import strings
from choice_list import ChoiceList

click.BaseCommand.ignore_unknown_options = True
click.BaseCommand.allow_extra_args = True


def _flatten_list_of_lists(l):
    return [item for sublist in l for item in sublist]


def _build_full_prompt(choice_list, prompt):
    for choice in choice_list:
        prompt += choice[1] + '\n'
    return prompt


project_type_cl = ChoiceList([
    strings.RESTFUL,
    strings.WEB_APP,
    strings.BOTH_RESTFUL_AND_WEB_APP,
])
RESTFUL_AND_OR_WEB_APP_PROMPT = _build_full_prompt(project_type_cl.choice_list,
                                                   "{}{}".format(strings.RESTFUL_AND_OR_WEB_APP_PROMPT_BASE, '\n'))

framework_lang_cl = ChoiceList([
    strings.JAVA_UNDERTOW,
    strings.ECMASCRIPT_EXPRESS,
    strings.SCALA_AKKA,
])
<<<<<<< HEAD

CHOOSE_API_FRAMEWORK_PROMPT = "{}{}".format(strings.CHOOSE_API_FRAMEWORK_PROMPT_BASE, '\n')
for choice in framework_lang_choices:
    CHOOSE_API_FRAMEWORK_PROMPT += choice[1] + '\n'

RESTFUL_AND_OR_WEB_APP_PROMPT = "{}{}".format(strings.RESTFUL_AND_OR_WEB_APP_PROMPT_BASE, '\n')
for choice in project_type_choices:
    RESTFUL_AND_OR_WEB_APP_PROMPT += choice[1] + '\n'
=======
CHOOSE_FRAMEWORK_PROMPT = _build_full_prompt(framework_lang_cl.choice_list,
                                             "{}{}".format(strings.CHOOSE_FRAMEWORK_PROMPT_BASE, '\n'))
>>>>>>> master


@click.command()
@click.option('--project-type',
              type=click.Choice(_flatten_list_of_lists(project_type_cl.choice_list)),
              prompt=RESTFUL_AND_OR_WEB_APP_PROMPT)
def jigsaw(project_type):
    project_type = project_type_cl.normalize(project_type)

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
<<<<<<< HEAD
              type=click.Choice(_flatten_list_of_lists(framework_lang_choices)),
              prompt=CHOOSE_API_FRAMEWORK_PROMPT)
=======
              type=click.Choice(_flatten_list_of_lists(framework_lang_cl.choice_list)),
              prompt=CHOOSE_FRAMEWORK_PROMPT)
>>>>>>> master
def setup_restful_api(framework_and_lang):
    framework_and_lang = framework_lang_cl.normalize(framework_and_lang)

    click.echo("Setting up {}".format(framework_and_lang))
    print

    # TODO finish


if __name__ == '__main__':
    jigsaw()
