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


class Corset(Package):
    """Corset is a command-line software program to go from a de novo
       transcriptome assembly to gene-level counts."""

    homepage = "https://github.com/Oshlack/Corset/wiki"
    url      = "https://github.com/Oshlack/Corset/releases/download/version-1.06/corset-1.06-linux64.tar.gz"

    version('1.06', '0a6d0bb1f2d1bdbcb8b47656a7f12f23')

    def url_for_version(self, version):
        url = 'https://github.com/Oshlack/Corset/releases/download/version-{0}/corset-{0}-linux64.tar.gz'
        return url.format(version)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('corset', prefix.bin)
        install('corset_fasta_ID_changer', prefix.bin)
