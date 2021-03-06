##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyPybind11(CMakePackage):
    """pybind11 -- Seamless operability between C++11 and Python.
    pybind11 is a lightweight header-only library that exposes C++ types in
    Python and vice versa, mainly to create Python bindings of existing C++
    code. Its goals and syntax are similar to the excellent Boost.Python
    library by David Abrahams: to minimize boilerplate code in traditional
    extension modules by inferring type information using compile-time
    introspection."""

    homepage = "https://pybind11.readthedocs.io"
    url      = "https://github.com/pybind/pybind11/archive/v2.1.0.tar.gz"

    version('2.1.1', '5518988698df937ccee53fb6ba91d12a')
    version('2.1.0', '3cf07043d677d200720c928569635e12')

    depends_on('py-pytest', type=('build'))

    extends('python')

    def cmake_args(self):
        args = []
        args.append('-DPYTHON_EXECUTABLE:FILEPATH=%s'
                    % self.spec['python'].command.path)
        return args
