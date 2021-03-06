# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg
from oslo.utils import importutils

keymgr_opts = [
    cfg.StrOpt('api_class',
               default='cinder.keymgr.conf_key_mgr.ConfKeyManager',
               help='The full class name of the key manager API class'),
]

CONF = cfg.CONF
CONF.register_opts(keymgr_opts, group='keymgr')


def API():
    cls = importutils.import_class(CONF.keymgr.api_class)
    return cls()
