## Map Coloring Problem - Map Picture Generator for visualizing CSP solutions (AI Lab)

<div align="center">
  <img src="https://github.com/m-LoKi-g/SI_CSP_MapGenerator/blob/master/map.png?raw=true" width=400px>
</div>

### Dependencies

- Python 3.8 (or newer)
- [Pillow](https://python-pillow.org)

### Installation

To install **Pillow** use following command in your terminal (assuming you have **Pip** installed):

```
pip install Pillow
```

### Usage

#### 1. Solution JSON file

First you need to generate yourself a solution JSON file in the format just like following example (contents of `example.json`):

```
{
  "board": 16,    // square board side size
  "regions": [    // list of regions represented by points on the board
    [6, 7],       // 0
    [14, 3],      // 1
    [5, 13],      // 2
    [12, 15]      // 3
  ],
  "colors": [1, 2, 2, 3], // colors of regions (indices in 'colors' list correspond with indices in 'regions' list)
  "connections": [ // list of 'regions' list indices that represents the regions the given region is connected with (ordering does not matter)
    [1, 2, 3],  // region 0 is connected with regions 1,2,3
    [0, 3],     // region 1 is connected with regions 0, 3
    [0, 3],     // region 2 and so on...
    [0, 1, 2]   // region 3 ...
  ]
}
```

Where:

- script uses cartesian coordinate system (Y axis is grows up and origin _(0,0)_ is placed in the bottom-left corner)


#### 2. Run script

Interface: `generator.py <input (*.json)> [<output (*.png)>]`

Options:

- `<input (*.json)>` - solution file in JSON format, i.e. `example.json` (obligatory).
- `[<output (*.png)>]` - path of the saved result file, i.e. `board.png` (optional - if not given then script will only show the result in the window without saving it).

##### Usage examples

```
>> python generator.py example.json map.png    ### result is saved to file named map.png

>> python generator.py example.json    ### result is only displayed in system window
```

### Extras

You can change the scale of generated image by modifying `SCALE` constant in `generator.py`.
