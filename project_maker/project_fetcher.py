#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from multiprocessing.pool import Pool
from git import Repo
import os

"""
This file holds the implementation for the class that returns an instance of a ProjectFetcher. ProjectFetchers expose a
two static methods: one for setting the project_dict and another for fetching projects. ProjectFetcher clones into the
current working directory for now.

Usage:
ProjectFetcher.set_project_dict(jigsaw_clone="https://github.com/webbusinessdeveloper/jigsaw.git",
                                express="https://github.com/webbusinessdeveloper/express-dir-structure.git")
repos = ProjectFetcher.fetch_projects("jigsaw_clone", "express")  # blocking call
"""

project_dict = dict()


class ProjectFetcher(object):
    @staticmethod
    def fetch_projects(*projects):
        pool = Pool(4)
        cloned_repos = pool.map(clone_repo, projects)
        pool.close()
        return cloned_repos

    @staticmethod
    def set_project_dict(**_project_dict):
        global project_dict
        project_dict = _project_dict


def clone_repo(project):
    return Repo.clone_from(project_dict[project], os.path.join(os.getcwd(), project))
