#!/usr/bin/env python3

  
"""
 @file
 @brief This class permits rendering from cli
 @author francesco-hermanitosverdes
 @author Matteo Gheza <matteo.gheza07@gmail.com>
 @section LICENSE
 Copyright (c) 2008-2018 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.
 OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys

try:
    from classes import cli_render
    print("Loaded modules from current directory: %s" % info.PATH)
except ImportError:
    import openshot_qt
    sys.path.append(openshot_qt.OPENSHOT_PATH)
    from classes import cli_render
    print("Loaded modules from installed directory: %s" % info.PATH)

def main():
	bot = cli_render.Bot()
	bot.render()
	sys.exit()

if __name__ == "__main__":
    main()
