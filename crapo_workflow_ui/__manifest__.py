# pylint: disable=missing-docstring
{
    "name": "Crapo: Workflow UI",
    "version": "12.0.3.0.0",
    "category": "Crapo Automata & Workflows",
    "author": "Article714",
    "license": "LGPL-3",
    "website": "https://www.article714.org",
    "summary": """ Add UI to crapo workflows """,
    "depends": ["crapo_workflow", "web_tree_dynamic_colored_field"],
    "data": [
        "actions/window_actions.xml",
        "views/crapo_menus.xml",
        "views/crapo_workflow_activity_views.xml",
        "views/crapo_workflow_views.xml",
        "views/crapo_workflow_event_views.xml",
        "views/crapo_workflow_trigger_views.xml",
        "views/crapo_workflow_context_views.xml",
        "security/workflow_diagram.xml",
    ],
    "installable": True,
    "images": [],
    "application": True,
}
