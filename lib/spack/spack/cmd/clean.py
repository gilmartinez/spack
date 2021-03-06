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
import argparse

import llnl.util.tty as tty

import spack
import spack.cmd

description = "remove temporary build files and/or downloaded archives"
section = "build"
level = "long"


class AllClean(argparse.Action):
    """Activates flags -s -d and -m simultaneously"""
    def __call__(self, parser, namespace, values, option_string=None):
        parser.parse_args(['-sdm'], namespace=namespace)


def setup_parser(subparser):
    subparser.add_argument(
        '-s', '--stage', action='store_true',
        help="remove all temporary build stages (default)")
    subparser.add_argument(
        '-d', '--downloads', action='store_true',
        help="remove cached downloads")
    subparser.add_argument(
        '-m', '--misc-cache', action='store_true',
        help="remove long-lived caches, like the virtual package index")
    subparser.add_argument(
        '-a', '--all', action=AllClean, help="equivalent to -sdm", nargs=0
    )
    subparser.add_argument(
        'specs',
        nargs=argparse.REMAINDER,
        help="removes the build stages and tarballs for specs"
    )


def clean(parser, args):

    # If nothing was set, activate the default
    if not any([args.specs, args.stage, args.downloads, args.misc_cache]):
        args.stage = True

    # Then do the cleaning falling through the cases
    if args.specs:
        specs = spack.cmd.parse_specs(args.specs, concretize=True)
        for spec in specs:
            msg = 'Cleaning build stage [{0}]'
            tty.msg(msg.format(spec.short_spec))
            package = spack.repo.get(spec)
            package.do_clean()

    if args.stage:
        tty.msg('Removing all temporary build stages')
        spack.stage.purge()

    if args.downloads:
        tty.msg('Removing cached downloads')
        spack.fetch_cache.destroy()

    if args.misc_cache:
        tty.msg('Removing cached information on repositories')
        spack.misc_cache.destroy()
