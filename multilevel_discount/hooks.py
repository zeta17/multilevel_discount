# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "multilevel_discount"
app_title = "Multilevel Discount"
app_publisher = "hendrik"
app_description = "Multilevel Discount"
app_icon = "fa fa-percent"
app_color = "#01dfa5"
app_email = "hendrik.zeta@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/multilevel_discount/css/multilevel_discount.css"
# app_include_js = "/assets/multilevel_discount/js/multilevel_discount.js"

# include js, css files in header of web template
# web_include_css = "/assets/multilevel_discount/css/multilevel_discount.css"
# web_include_js = "/assets/multilevel_discount/js/multilevel_discount.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "multilevel_discount.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "multilevel_discount.install.before_install"
# after_install = "multilevel_discount.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "multilevel_discount.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"multilevel_discount.tasks.all"
# 	],
# 	"daily": [
# 		"multilevel_discount.tasks.daily"
# 	],
# 	"hourly": [
# 		"multilevel_discount.tasks.hourly"
# 	],
# 	"weekly": [
# 		"multilevel_discount.tasks.weekly"
# 	]
# 	"monthly": [
# 		"multilevel_discount.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "multilevel_discount.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "multilevel_discount.event.get_events"
# }

