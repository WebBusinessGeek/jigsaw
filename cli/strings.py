# -*- coding: utf-8 -*-

RESTFUL_AND_OR_WEB_APP_PROMPT_BASE = \
    """Please select a project type"""

RESTFUL = \
    """RESTful API"""

WEB_APP = \
    """Client-side web app"""

BOTH_RESTFUL_AND_WEB_APP = "{} & {}".format(RESTFUL, WEB_APP)

CHOOSE_FRAMEWORK_PROMPT_BASE = \
    """Please select a framework and programming language pair"""

ECMASCRIPT_EXPRESS = \
    """ECMAScript and Express"""

JAVA_UNDERTOW = \
    """Java and Undertow"""

SCALA_AKKA = \
    """Scala and Akka"""

CLOJURE_COMPOJURE = \
    """Clojure and Compojure"""

GO_GIN = \
    """Go and Gin"""

PYTHON_BOTTLE = \
    """Python and Bottle"""

RUBY_SINATRA = \
    """Ruby and Sinatra"""
