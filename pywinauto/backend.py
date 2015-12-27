# GUI Application automation and testing library
# Copyright (C) 2016 Vasily Ryabov
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

"""Back-end components storage (links to platform-specific things)"""

from .NativeElementInfo import NativeElementInfo
from .controls.HwndWrapper import HwndWrapper

registered_backends = {
    'native': (NativeElementInfo, HwndWrapper, ),
}

from .sysinfo import UIA_support
if UIA_support:
    from .UIAElementInfo import UIAElementInfo
    from .controls.ElementWrapper import ElementWrapper
    registered_backends['uia'] = (UIAElementInfo, ElementWrapper, )

active_name = 'native'
ActiveElementInfo = NativeElementInfo
ActiveWrapper = HwndWrapper

def set(new_active_name):
    """
    Set active back-end by name

    Possible values of **active_name** are "native", "uia" or
    other name registered by the **register** function.
    """
    if new_active_name not in registered_backends.keys():
        raise ValueError('Back-end "{backend}" is not registered!'.format(backend=new_active_name))

    global active_name
    active_name = new_active_name
    global ActiveElementInfo, ActiveWrapper
    (ActiveElementInfo, ActiveWrapper) = registered_backends[new_active_name]

def register(backend_name, wrapper):
    pass