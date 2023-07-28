# Reddit r/place 2023 Timelapse Generator for Tiles

This application generates the HD Timelapse video for Reddit r/place 2023.


## Usage

1. Go to the `reference` folder and find `frame_id` with the 4 boundary positions of the target tile. For instance, the Genshin Impact tile is located in frame `4`, with `left=400`, `upper=240`, `right=530` and `lower=360`

2. In this folder, run the command `python -m pip install -r requirements.txt` to install dependencies.

3. run `python .\get_tiles.py [frame_id] [left] [upper] [right] [lower]` to download the clipped image sequence. For instance, to download the Genshin Impact tile, the command should be `python .\get_tiles.py 4 400 240 530 360`. The files will be stored in `.\output` folder, or you can pass a custom `--output` command.

## Video generation

To generate a video, you should first install [FFmpeg](https://github.com/FFmpeg/FFmpeg) and add it to `PATH`.

The basic command is `ffmpeg -framerate 60 -i ./output/%05d.png -c:v libx264 -pix_fmt yuv420p output.mp4`, which will generate a timelapse video at 3600 timescales (1 second for 1 hour).
You can change the timescale by modifying `framerate`

To upscale the video, pass `-vf scale=iw*2:ih*2:flags=neighbor` to the command, where `2` is the scale ratio.
For instance, `ffmpeg -framerate 60 -i ./output/%05d.png -vf scale=iw*10:ih*10:flags=neighbor -c:v libx264 -pix_fmt yuv420p output.mp4` generates a 1300x1200 Genshin Impact video

## Example

https://www.reddit.com/r/Genshin_Impact/comments/159xt5t/an_hd_timelapse_for_genshin_impact_in_rplace_2023/

## Use different time margin

The database is sampled every minute. If you want to generate video with finer scale, you can re-query the image urls from reddit.com.
The query method and sample code can be seen [here](https://github.com/AS042971/rplace-2023-tile-timelapse/issues/1#issuecomment-1656358900)
