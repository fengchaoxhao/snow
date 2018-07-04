from colormath.color_conversions import convert_color
from colormath.color_objects import LCHabColor,sRGBColor

def tohex(l,c,h):
  rgb = convert_color(LCHabColor(l,c,h),sRGBColor)
  clamp = sRGBColor(rgb.clamped_rgb_r, rgb.clamped_rgb_g, rgb.clamped_rgb_b)
  return clamp.get_rgb_hex()

hexgry0_lt = tohex( 12.00/12.0*100.0 , 00.00/12.0*100 , 255.00 )
hexgry1_lt = tohex( 11.25/12.0*100.0 , 00.25/12.0*100 , 255.00 )
hexgry2_lt = tohex( 05.94/12.0*100.0 , 01.50/12.0*100 , 255.00 )
hexgry3_lt = tohex( 04.48/12.0*100.0 , 01.50/12.0*100 , 255.00 )

hexred__lt = tohex( 06.06/12.0*100.0 , 08.50/12.0*100 , 030.00 )
hexyllw_lt = tohex( 10.50/12.0*100.0 , 12.00/12.0*100 , 090.00 )
hexgren_lt = tohex( 05.99/12.0*100.0 , 08.50/12.0*100 , 135.00 )
hexblue_lt = tohex( 05.63/12.0*100.0 , 08.50/12.0*100 , 270.00 )

hexgry0_dk = tohex( 02.00/12.0*100.0 , 01.00/12.0*100 , 255.00 )
hexgry1_dk = tohex( 02.75/12.0*100.0 , 01.25/12.0*100 , 255.00 )
hexgry2_dk = tohex( 07.11/12.0*100.0 , 01.50/12.0*100 , 255.00 )
hexgry3_dk = tohex( 08.76/12.0*100.0 , 01.50/12.0*100 , 255.00 )

hexred__dk = tohex( 07.18/12.0*100.0 , 03.50/12.0*100 , 030.00 )
hexyllw_dk = tohex( 09.50/12.0*100.0 , 06.00/12.0*100 , 090.00 )
hexgren_dk = tohex( 07.16/12.0*100.0 , 03.50/12.0*100 , 135.00 )
hexblue_dk = tohex( 07.09/12.0*100.0 , 03.50/12.0*100 , 270.00 )

print '# general'
print 'Author:          nightsense'
print 'Maintainer:      nightsense'
print 'License:         MIT'
print 'Full name:       snow'
print 'Short name:      snow'
print 'Terminal Colors: 256'
print ''
print '# light'
print 'Background: light'
print 'Color:      gry0 %s ~' % hexgry0_lt
print 'Color:      gry1 %s ~' % hexgry1_lt
print 'Color:      gry2 %s ~' % hexgry2_lt
print 'Color:      gry3 %s ~' % hexgry3_lt
print 'Color:      gry4 %s ~' % hexgry0_dk
print 'Color:      red_ %s ~' % hexred__lt
print 'Color:      yllw %s ~' % hexyllw_lt
print 'Color:      gren %s ~' % hexgren_lt
print 'Color:      blue %s ~' % hexblue_lt
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gry4 reverse'
print 'DiffText    yllw gry4 reverse'
print 'MatchParen  yllw gry4 reverse'
print 'Search      yllw gry4 reverse'
print ''
print '# dark'
print 'Background: dark'
print 'Color:      gry0 %s ~' % hexgry0_dk
print 'Color:      gry1 %s ~' % hexgry1_dk
print 'Color:      gry2 %s ~' % hexgry2_dk
print 'Color:      gry3 %s ~' % hexgry3_dk
print 'Color:      gry4 %s ~' % hexgry3_dk
print 'Color:      red_ %s ~' % hexred__dk
print 'Color:      yllw %s ~' % hexyllw_dk
print 'Color:      gren %s ~' % hexgren_dk
print 'Color:      blue %s ~' % hexblue_dk
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gry0 reverse'
print 'DiffText    yllw gry0 reverse'
print 'MatchParen  yllw gry0 reverse'
print 'Search      yllw gry0 reverse'
