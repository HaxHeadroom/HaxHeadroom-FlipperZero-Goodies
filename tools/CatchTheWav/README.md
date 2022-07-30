![header-logos](https://img.shields.io/website?color=alert&down_color=offline&down_message=offline&label=maxheadroom.dev&logo=Hyperledger&up_color=online&up_message=online&url=https%3A%2F%2Fmaxheadroom.dev%2F)
![header-logos](https://img.shields.io/static/v1?label=Firmware&logo=dev.to&message=Staging&color=9cf)
![header-logos](https://img.shields.io/static/v1?label=Version&logo=confluence&message=.23&color=green)
![header-logos](https://img.shields.io/github/commit-activity/w/HaxHeadroom/HaxHeadroom-FlipperZero-Goodies)

`HaxHeadroom Firmware is live:` https://github.com/HaxHeadroom/HaxHeadroom-FlipperZero-firmware-wPlugins/releases

```python
                                           ▒▓░                                           
                                       ▓▓  ▒▓▒▒▓▓▓                                        
                                   ░            ▓▓▓▓▓                                     
                                 ░░            ▓▓▓▓▓▓▓▓░                                  
                                ░           ▒▓▓▓▓▓▓▓▓▓▓▓                         
                              ▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                             
                              ▒▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                 
                               ░▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                 
                                  ▓░ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   𝚝-𝚝-𝚝-𝚝-𝚝𝚞𝚗𝚎 𝚢𝚘𝚞𝚛 𝚏-𝚏-𝚏𝚕𝚒𝚙𝚙𝚎𝚛 𝚒𝚗𝚝𝚘 𝙽𝚎𝚝𝚠𝚘𝚛𝚔 𝟸𝟹!                          
                               ▓          ▒▓░  ▓▓▓▓▓▓▓▓▓▓░   Send the wav!                         
                              ▓          ▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓                                 
                              ▓      ▒▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓                                 
                                   ░▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓░                                
                               ▒   ▓▓▓▓▓▓▓▓▓▓ ▒▓▓▓▓▓▓▓▓▓▓▓                                
                                     ▒    ▓▓▓ ▒▓▓▓▓▓▓▓▓▓▓▓                                
                               ▓          ▒▓░▒▓▓▓▓▓▓▓▓▓▓                                  
                               ▒         ▒▓▓▓▓▓▓▓▓▓▓▓                                     
                               ░▓      ░▓▓▓▓▓▓▓▓▓▓▓▓▓                                     
                                 ▒    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                     
                                 ▓    ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                     
                                ▒▓      ░▓▓▓▓▓▓▓▓▓▓▓▓                                     
                              ░░         ▒▓▓▓▓▓▓▓▓▓▓▓░▓░                                  
                              ▓▓         ▓▓▓▓▓▓   ▓▓▓▓▓ ▓░                                
                            ▓▒  ▒        ░▓▓░     ░▓▓▓░   ▓░                              
                          ▓░    ▓▒     ▓      ▒    ▒▓▓      ▓░                            
                     ▓▓░        ░▓░  ▓▓       ░▓     ▓        ▓▓░                         
                ▓▓░               ▓░   ▓░     ▒▓    ▓░            ░▓▓░                    
          ░▓▓                      ▓    ░░   ░▒     ▓                   ░▓                
      ▓▓                            ▒   ▓     ▒     ▓                         ▓░          
    ░                               ▓  ▒░     ▓    ▒  I shouldnt be a repo       ▓░ 


```
![header-logos](https://github.com/HaxHeadroom/HaxHeadroom-FlipperZero-Goodies/raw/main/tools/CatchTheWav/SendTheWav.gif)


`Step 0`

```
pip3 install img2wav
```

`Step 1`

```
$ img2wav --help
usage: img2wav [-h] [-o OUTPUT] [-d DELAY] [-f FREQUENCY] [-b BANDWIDTH]
               [-s SAMPLERATE]
               images [images ...]

Convert images to a wav file to display in a spectrogram. If multiple images
are specified, combine them into a single wav file.

positional arguments:
  images                8-bit bmp images to process

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file to write the wav to (default: img.wav)
  -d DELAY, --delay DELAY
                        Delay in ms between images when more than one is
                        specified (default: 2000)
  -f FREQUENCY, --frequency FREQUENCY
                        Center frequency for audio output signal (default:
                        2750)
  -b BANDWIDTH, --bandwidth BANDWIDTH
                        Bandwidth for audio output signal (default 4000)
  -s SAMPLERATE, --samplerate SAMPLERATE
                        Sample rate for audio output signal (default 11025)
```

`Step 2`

```
copy wav to flipper
```

`Some examples`

```
$ img2wav examples/CatchTheWave.png -o examples/SendThe.wav  -s 24100 -f 2500
```
