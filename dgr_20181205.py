Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/atvasinajums.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/atvasinajums.py', 'sys': <module 'sys' (built-in)>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f171c049e18>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f171c049e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])}
>>> type(x)
<class 'numpy.ndarray'>
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> x[0]
0.0
>>> x[2]
0.8
>>> x[10]
4.0
>>> x[11]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[11]
IndexError: index 11 is out of bounds for axis 0 with size 11
>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> y
array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])
>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/atvasinajums.py", line 13, in <module>
    from mathplotlib import pyplot as plt
ModuleNotFoundError: No module named 'mathplotlib'
>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================
['$sin(x)$ - default - viss ir savienots ar taisnam liinijaam']
['$sin(x)$ - default - viss ir savienots ar taisnam liinijaam', '$sin(x)$ - tikai dazhi punkti']

================= RESTART: /home/user/RTR105/atvasinajums.py =================
>>> print(plt.__doc__)

`matplotlib.pyplot` is a state-based interface to matplotlib. It provides
a MATLAB-like way of plotting.

pyplot is mainly intended for interactive plots and simple cases of programmatic
plot generation::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

The object-oriented API is recommended for more complex plots.

>>> print(plt.plot__doc__)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(plt.plot__doc__)
AttributeError: module 'matplotlib.pyplot' has no attribute 'plot__doc__'
>>> print(plt.plot.__doc__)
Plot lines and/or markers to the
:class:`~matplotlib.axes.Axes`.  *args* is a variable length
argument, allowing for multiple *x*, *y* pairs with an
optional format string.  For example, each of the following is
legal::

    plot(x, y)        # plot x and y using default line style and color
    plot(x, y, 'bo')  # plot x and y using blue circle markers
    plot(y)           # plot y using x as index array 0..N-1
    plot(y, 'r+')     # ditto, but with red plusses

If *x* and/or *y* is 2-dimensional, then the corresponding columns
will be plotted.

If used with labeled data, make sure that the color spec is not
included as an element in data, as otherwise the last case
``plot("v","r", data={"v":..., "r":...)``
can be interpreted as the first case which would do ``plot(v, r)``
using the default line style and color.

If not used with labeled data (i.e., without a data argument),
an arbitrary number of *x*, *y*, *fmt* groups can be specified, as in::

    a.plot(x1, y1, 'g^', x2, y2, 'g-')

Return value is a list of lines that were added.

By default, each line is assigned a different style specified by a
'style cycle'.  To change this behavior, you can edit the
axes.prop_cycle rcParam.

The following format string characters are accepted to control
the line style or marker:

================    ===============================
character           description
================    ===============================
``'-'``             solid line style
``'--'``            dashed line style
``'-.'``            dash-dot line style
``':'``             dotted line style
``'.'``             point marker
``','``             pixel marker
``'o'``             circle marker
``'v'``             triangle_down marker
``'^'``             triangle_up marker
``'<'``             triangle_left marker
``'>'``             triangle_right marker
``'1'``             tri_down marker
``'2'``             tri_up marker
``'3'``             tri_left marker
``'4'``             tri_right marker
``'s'``             square marker
``'p'``             pentagon marker
``'*'``             star marker
``'h'``             hexagon1 marker
``'H'``             hexagon2 marker
``'+'``             plus marker
``'x'``             x marker
``'D'``             diamond marker
``'d'``             thin_diamond marker
``'|'``             vline marker
``'_'``             hline marker
================    ===============================


The following color abbreviations are supported:

==========  ========
character   color
==========  ========
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
==========  ========

In addition, you can specify colors in many weird and
wonderful ways, including full names (``'green'``), hex
strings (``'#008000'``), RGB or RGBA tuples (``(0,1,0,1)``) or
grayscale intensities as a string (``'0.8'``).  Of these, the
string specifications can be used in place of a ``fmt`` group,
but the tuple forms can be used only as ``kwargs``.

Line styles and colors are combined in a single format string, as in
``'bo'`` for blue circles.

The *kwargs* can be used to set line properties (any property that has
a ``set_*`` method).  You can use this to set a line label (for auto
legends), linewidth, anitialising, marker face color, etc.  Here is an
example::

    plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
    plot([1,2,3], [1,4,9], 'rs',  label='line 2')
    axis([0, 4, 0, 10])
    legend()

If you make multiple lines with one plot command, the kwargs
apply to all those lines, e.g.::

    plot(x1, y1, x2, y2, antialiased=False)

Neither line will be antialiased.

You do not need to use format strings, which are just
abbreviations.  All of the line properties can be controlled
by keyword arguments.  For example, you can set the color,
marker, linestyle, and markercolor with::

    plot(x, y, color='green', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=12).

See :class:`~matplotlib.lines.Line2D` for details.

The kwargs are :class:`~matplotlib.lines.Line2D` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

kwargs *scalex* and *scaley*, if defined, are passed on to
:meth:`~matplotlib.axes.Axes.autoscale_view` to determine
whether the *x* and *y* axes are autoscaled; the default is
*True*.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.



>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/atvasinajums.py", line 39, in <module>
    plot.plot(x,derivative,"y")
NameError: name 'plot' is not defined
>>> 
================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================

================= RESTART: /home/user/RTR105/atvasinajums.py =================
>>> 
