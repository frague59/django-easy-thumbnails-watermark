INSTALL
=======

put easy_thumbnails_watermark in INSTALLED_APPS

::

    INSTALLED_APPS = (
        'easy_thumbnails_watermark',
    )

add the watermark preprocesor in your settings

::

    from easy_thumbnails.conf import Settings as easy_thumbnails_defaults

    THUMBNAIL_PROCESSORS = easy_thumbnails_defaults.THUMBNAIL_PROCESSORS + (
        'easy_thumbnails_watermark.thumbnail_processors.watermark_processor',
    )

and add 'WATERMARK': , to your thumbnail definition for easy_thumbnails.

::

        'thumb': {
            ...
            'WATERMARK': { 
                'image': 'main/img/logo.png',
                'opacity': 0.2,
                'scale': '40%',
            },
            ...
        },

And one of the following settings:

* ``image`` - A path to an image in your static files folder
* ``position`` - Specify the relative position in one of four image corners ``BR``, ``BL``,
    ``TR``, and ``TL``.  These represent 'bottom-right', 'bottom-left', 'top-right', and 'top-left' respectively.
    
  Alternatively, you can use relative or absolute positioning for the
  watermark.  Relative positioning uses percentages; absolute positioning uses
  exact pixels.  You can mix and match these two modes of positioning, but you
  cannot mix and match relative/absolute with the corner positioning.  When
  using relative/absolute positioning, the value for the ``position`` parameter
  is ``XxY``, where ``X`` is the left value and ``Y`` is the top value.  The
  left and top values must be separated with a lowercase ``x``.

  If you wanted your watermark image to show up in the center of any image you
  want to watermark, you would use a position parameter such as
  ``position=50%x50%`` or even ``position=C``.  If you wanted the watermark to
  show up half-way between the left and right edges of the image and 100 pixels
  from the top, you would use a position parameter such as
  ``position=50%x100``. 

  Finally, you may tell the filter to generate a position for your watermark
  dynamically.  To do this, use ``position=R``.
* ``opacity`` - This parameter allows you to specify the transparency of the
  applied watermark.  The value must be an integer between 0 and 1, where 0
  is fully transparent and 1 is fully opaque.  By default, the opacity is set
  at 0.5.
* ``tile`` - If you want your watermark to tile across the entire image, you
  simply specify a parameter such as ``tile=1``.
* ``scale`` - If you'd like to have the watermark as big as possible on the
  target image and fully visible, you might want to use ``scale=F``.  If you
  want to specify a particular scaling factor, just use something like
  ``scale=1.43``.
  Scale could also be a percentage of the smallest image, the one to be watermarked,
  dimension, for example '20%' would scale the watermark to be 20% of the smallest
  between width and height of the target image.
* ``greyscale`` - If you want your watermark to be greyscale, you can specify
  the parameter ``greyscale=1`` and all color saturation will go away.
* ``rotation`` - Set this parameter to any integer between 0 and 359 (really
  any integer should work, but for your own sanity I recommend keeping the
  value between 0 and 359).  If you want the rotation to be random, use
  ``rotation=R`` instead of an integer.
* ``noalpha`` defaults to False, removes any alpha introduced with the watermark effect, useful to force a jpg image to remain the same, saving a lot of space, setting to True effectively converts any RGBA color space to RGB.

They defaults to  watermark=False, position='C', opacity=100, scale=1, tile=False, greyscale=False, rotation=0

Credits
=======

I copied various code from https://raw.github.com/codekoala/django-watermark
and simply adapted for easy_thumbnails

