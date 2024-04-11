##################################YUNYOO.CN####################################
#                                                                             *
# AUTO GENERTATED VMPStudio PLUGIN PYTHON INTERFACE FILE                      *
#                                                                             *
# Copyright(C) 2022 YunYoo Corp., ALL RIGHTS RESERVED.                        *
#                                                                             *
# Internet: yunyoo.cn                                                         *
#                                                                             *
# This code is distributed "as is", part of VMPStudio and without warranty of *
# any kind, expressed or implied, including, but not limited to warranty of   *
# fitness for any particular purpose. In no event will VMPStudio be liable to *
# you for any special, incidental, indirect, consequential or any other       *
# damages caused by the use, misuse, or the inability to use of this code,    *
# including anylost profits or lost savings,even if VMPStudio has been advised*
# of the possibility of such damages.                                         *
#                                                                             *
######################################*#######################################/

# keys for vsp_on_event args
vsp_inkey_name = 'name' # plugin module name
vsp_inkey_type = 'event' # event type
vsp_inkey_value = 'value' # event payload
vsp_outkey_error = 'error' # return error code
vsp_outkey_result = 'result' # return value

vsp_arch_unsupport = 0
vsp_arch_armv5te = 1
vsp_arch_arm = 2
vsp_arch_arm64 = 3
vsp_arch_x86 = 4
vsp_arch_x64 = 5

vsp_version = '1.0.0'

vsp_err_ok = 0 # success
vsp_err_failed = 1 # failed
vsp_err_canceled = 2 # canceled
vsp_err_param = 3 # bad parameter
vsp_err_notfound = 4 # cannot find something
vsp_err_io = 5 # io issue
vsp_err_thread = 6 # thread issue, some api must run at ui thread
vsp_err_oor = 7 # out of range
vsp_err_oom = 8 # out of memory
vsp_err_auth = 9 # license issue
vsp_err_permission = 10 # permission issue
vsp_err_unsupport = 11 # unsupport some action
vsp_err_unimpl = 12 # unimplement some action
vsp_err_softbug = 13 # software bug assertion
vsp_err_continue = 14 # for traverser
vsp_err_break = 15 # for traverser

vsp_event_loaded = 0 # after loaded this plugin
vsp_event_pre_unload = 1 # before unload this plugin
vsp_event_main_menu = 2 # user triggered MainMenu/Plugin/ThisPlugin
vsp_event_module_analyzed = 3 # tell plugin finished analyzing an file module
vsp_event_module_closed = 4 # tell plugin closed the module
vsp_event_sample_initialized = 5 # tell plugin a new uvm sample session initialized
vsp_event_version = 6 # ask this plugin for its sdk version
vsp_event_menuname = 7 # ask this plugin for its plugin menu name
vsp_event_vspinfo = 8 # ask this plugin for its self version and description

