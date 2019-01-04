"""This software is for stitching images created by Dark Spot Mapper

Dark Spot Mapper is a measurement device at the Optoelectronics Research Centre of Tampere University of Technology

Copyright 2017-2019 Mika Mäki & Tampere University of Technology
Mika would like to license this program with GPLv3+ but it would require some university bureaucracy
"""

import tkinter.filedialog
import os


def main():
    wafer_path = tkinter.filedialog.askdirectory()

    if wafer_path != "":
        print("Stitching wafer")
        cmdstr = "magick convert background_wafer.png "
        cmdstr += wafer_path + "/00x20/*stitch.png -gravity Northwest -geometry +5800+0 -composite "
        cmdstr += wafer_path + "/00x10/*stitch.png -geometry +5800+2580 -composite "
        cmdstr += wafer_path + "/-10x10/*stitch.png -geometry +2900+2580 -composite "
        cmdstr += wafer_path + "/10x10/*stitch.png -geometry +8700+2580 -composite "
        cmdstr += wafer_path + "/00x00/*stitch.png -geometry +5800+5160 -composite "
        cmdstr += wafer_path + "/-20x00/*stitch.png -geometry +0+5160 -composite "
        cmdstr += wafer_path + "/-10x00/*stitch.png -geometry +2900+5160 -composite "
        cmdstr += wafer_path + "/10x00/*stitch.png -geometry +8700+5160 -composite "
        cmdstr += wafer_path + "/20x00/*stitch.png -geometry +11600+5160 -composite "
        cmdstr += wafer_path + "/00x-10/*stitch.png -geometry +5800+7740 -composite "
        cmdstr += wafer_path + "/-10x-10/*stitch.png -geometry +2900+7740 -composite "
        cmdstr += wafer_path + "/10x-10/*stitch.png -geometry +8700+7740 -composite "
        cmdstr += wafer_path + "/00x-20/*stitch.png -geometry +5800+10320 -composite "
        cmdstr += wafer_path + "/WAFER_stitch.png"
        os.system(cmdstr)
        print("Stitch ready")


if __name__ == "__main__":
    main()
