#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2021 Grant Hadlich
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from datetime import datetime
import os
from urllib.request import urlretrieve
from twitterutils.twitterutils import tweet

# Globals
animation_dir = "./animations"

def tweet_sun_images():
    """ Sends a tweet about the SOHO Sun Observatory """
    try:
        now = datetime.now()
        time_ran = now.strftime("%-I:%M %p")
        os.makedirs(animation_dir, exist_ok=True)

        listing = [
                  (f"Here are the latest images from our #Sun on {now}! This movie cycles through the latest images each highlighting a wavelength. Individual movies in replies!\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_fade.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 94 Angstrom wavelength. As per #NASA, this highlights regions of the corona during a solar flare.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0094.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 131 Angstrom wavelength. As per #NASA, this highlights hottest material in a flare.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0131.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 171 Angstrom wavelength. As per #NASA, this highlights the sun's atmosphere, or corona, when quiet. It also shows giant magnetic arcs known as coronal loops.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0171.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 193 Angstrom wavelength. As per #NASA, this highlights a slightly hotter region of the corona and also the much hotter material of a solar flare.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0193.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 211 Angstrom wavelength. As per #NASA, this highlights shows the hotter, magnetically active regions in the sun's corona.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0211.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 304 Angstrom wavelength. As per #NASA, this highlights light that is emitted from the chromosphere and transition region.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0304.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 335 Angstrom wavelength. As per #NASA, this highlights, like 211, shows hotter, magnetically active regions in the corona.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0335.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 1600 Angstrom wavelength. As per #NASA, this highlights a mixture of the upper photosphere, the transition region between the chromosphere, and the corona.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_1600.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 1700 Angstrom wavelength. As per #NASA, this highlights the surface of the sun and the chromosphere, which lies just above the photosphere.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_1700.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 94, 193, and 335 Angstrom wavelengths.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_094335193.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 171, 193, and 211 Angstrom wavelengths.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_211193171.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the 171, 211, and 304 Angstrom wavelengths.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_304211171.mp4"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the #LASCO C2 #Coronagraph.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sohowww.nascom.nasa.gov/data/LATEST/current_c2.gif"),
                  (f"Here are the latest images from our #Sun on {now}! This movie highlights the #LASCO C3 #Coronagraph.\nCredits: #NASA #ESA #SOHO #SDO #SWPC", "https://sohowww.nascom.nasa.gov/data/LATEST/current_c3.gif")]

        previous_id = None

        for tweet_text, url in listing:
            try:
                filename = url.split("/")[-1]
                save_path = os.path.abspath(os.path.join(animation_dir, filename))

                # Download File
                urlretrieve(url, save_path)

                if (os.path.exists(save_path) == True):
                    # Tweet Image
                    previous_id = tweet(tweet_text, image_path=save_path, in_reply_to_status_id=previous_id, enable_tweet=True)

                    os.remove(save_path)
                else:
                    print(f"Failed Downloading: {filename}" )
            except:
                print(f"Failed Tweeting: {filename}" )

    except Exception as e:
        print(f"Failed Run: {time_ran}\n" + str(e))
