let g:airline#themes#snow#palette = {}

if &background ==# 'light'
  let s:gry0 = [ '#ffffff', 231 ]
  let s:gry1 = [ '#ebedf1', 255 ]
  let s:gry2 = [ '#67788a', 67  ]
  let s:gryy = [ '#202a35', 236 ]
  let s:red_ = [ '#d83c41', 167 ]
  let s:gren = [ '#018a08', 28  ]
  let s:blue = [ '#0074e8', 33  ]
else
  let s:gry0 = [ '#202a35', 235 ]
  let s:gry1 = [ '#2b3846', 237 ]
  let s:gry2 = [ '#a4b6c9', 110 ]
  let s:gryy = [ '#202a35', 235 ]
  let s:red_ = [ '#c07f78', 174 ]
  let s:gren = [ '#749a6a', 65  ]
  let s:blue = [ '#7590c1', 67  ]
endif

let s:nrm1 = [ s:gry0[0] , s:gry2[0] , s:gry0[1] , s:gry2[1] ]
let s:nrm2 = [ s:gry2[0] , s:gry1[0] , s:gry2[1] , s:gry1[1] ]
let s:insr = [ s:gry0[0] , s:gren[0] , s:gry0[1] , s:gren[1] ]
let s:visl = [ s:gry0[0] , s:blue[0] , s:gry0[1] , s:blue[1] ]
let s:rplc = [ s:gry0[0] , s:red_[0] , s:gry0[1] , s:red_[1] ]
let s:inac = [ s:gry2[0] , s:gry1[0] , s:gry2[1] , s:gry1[1] ]

let g:airline#themes#snow#palette.normal =
  \ airline#themes#generate_color_map( s:nrm1 , s:nrm2 , s:nrm2 )

let g:airline#themes#snow#palette.insert =
  \ airline#themes#generate_color_map( s:insr , s:nrm2 , s:nrm2 )

let g:airline#themes#snow#palette.visual =
  \ airline#themes#generate_color_map( s:visl , s:nrm2 , s:nrm2 )

let g:airline#themes#snow#palette.replace =
  \ airline#themes#generate_color_map( s:rplc , s:nrm2 , s:nrm2 )

let g:airline#themes#snow#palette.inactive =
  \ airline#themes#generate_color_map( s:inac , s:inac , s:inac )

let g:airline#themes#snow#palette.ctrlp =
  \ airline#extensions#ctrlp#generate_color_map( s:nrm2 , s:nrm1 , s:nrm2 )
