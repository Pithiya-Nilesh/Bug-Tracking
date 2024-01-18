app_name = "bug_tracking"
app_title = "Bug Tracking"
app_publisher = "Sanskar Technolab"
app_description = "This app For Tracking Bug"
app_email = "nilesh@sanskartechnolab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bug_tracking/css/bug_tracking.css"
# app_include_js = "/assets/bug_tracking/js/bug_tracking.js"

# include js, css files in header of web template
# web_include_css = "/assets/bug_tracking/css/bug_tracking.css"
# web_include_js = "/assets/bug_tracking/js/bug_tracking.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bug_tracking/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

fixtures = [
    {"dt": "DocPerm", "filters": [["name", "in", ["Bug Tracking"]]]},
    {"dt": "Bug Type"}
]

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bug_tracking/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bug_tracking.utils.jinja_methods",
# 	"filters": "bug_tracking.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bug_tracking.install.before_install"
# after_install = "bug_tracking.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bug_tracking.uninstall.before_uninstall"
# after_uninstall = "bug_tracking.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bug_tracking.utils.before_app_install"
# after_app_install = "bug_tracking.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bug_tracking.utils.before_app_uninstall"
# after_app_uninstall = "bug_tracking.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bug_tracking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bug_tracking.tasks.all"
# 	],
# 	"daily": [
# 		"bug_tracking.tasks.daily"
# 	],
# 	"hourly": [
# 		"bug_tracking.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bug_tracking.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bug_tracking.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bug_tracking.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bug_tracking.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bug_tracking.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bug_tracking.utils.before_request"]
# after_request = ["bug_tracking.utils.after_request"]

# Job Events
# ----------
# before_job = ["bug_tracking.utils.before_job"]
# after_job = ["bug_tracking.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bug_tracking.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

