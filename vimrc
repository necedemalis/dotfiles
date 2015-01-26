".vimrc

"Basic Settings
        let mapleader=","              ", statt \ als leader key
        "Background Theme 
        silent! colorscheme solarized  "silent! colorscheme ChocolateLiquor
        set background=dark
        "Detect file types
        filetype on
        filetype plugin on
        filetype plugin indent on
        syntax on
        "set
        set tw=96
        set history=50                 " keep 50 lines of command line history
        set backspace=indent,eol,start " more powerful backspacing
        set nocompatible               " Use Vim defaults instead of 100% vi compatibility
        set ruler                      " show
        set hls ic is                  " Search: Highlight, ignore case, show
        set smartcase                  " ignore case if search pattern is all lowercase
        set nocp                       " nocompatible
        set et                         " expandtab
        set smarttab                   " Insert tabs at the start of a line
        set breakindent                " Indent soft wrapped lines
        set showbreak=>>
        set tabstop=4
        set shiftwidth=4
        set autochdir                  " Change to same dir as file
        set visualbell                 " Visuelles Piepen
        set noerrorbells               " don't beep
        set hidden                     " zwischen Buffern wechseln ohne speichern zu müssen
        set autowrite                  " speichert Datei automatisch beim wechseln
        set spelllang=en,de            " Sprachen für Rechtschreibüberprüfung: Deutsch, English
        if has('gui_running')
                set guioptions-=T      " Versteckt GUI-Toolbar
                set guioptions-=m      " Versteckt GUI-Toolbar
        endif
        set autoindent                 " Copy indent from current line when starting a new line
        set go+=c                      " No Popup-Dialogs
        set shortmess+=I               " Keine Startup-Message
        set formatprg=par\ -w96        " Par für Umbruchformatierung mit Alt+q
        set autochdir                  " Change working directory to directory of current file
        set nolist
        set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc " Suffixes that get lower priority when doing tab completion for filenames
        set wildignore=*.swp,*.bak,*.pyc,*.class "ignore some file extensions when completing names by pressing Tab,
        "Unnamed register to plus register (system clipboard)
        if has('unnamedplus') 
          set clipboard=unnamed,unnamedplus
        endif
        "Save/Load manual made Folds
        au BufWinLeave * silent! mkview
        au BufWinEnter * silent! loadview
        "Backup
        set backup
        set noswapfile
        set backupdir=~/.vim/.backup,/tmp
        set directory=~/.vim/.backup,/tmp
        set writebackup

" Custom Keymapping
        "Leader Keymapping
        "Plugins
        "ct -> Command-T
        nnoremap <silent> <Leader>ct :silent! CommandT<CR>
        "fd -> FoldDigest()
        nmap <silent> <leader>fd :silent! call FoldDigest ()<cr>
        "nt -> :NerdTree
        nmap <silent> <leader>nt :silent! NERDTree<cr>
        "tb -> :Tagbar
        map <silent> <leader>tb :silent! Tagbar<cr> 
        "tl -> :TaskList
        map <silent> <leader>tl :silent! TaskList<cr> 
        "Prose/Code
        "pr -> :Prose
        nmap <silent> <leader>pr :Prose<cr>
        "co -> :Code
        nmap <silent> <leader>co :Code<cr>
        "Buffer commands
        "bs -> zeigt Buffer an
        nmap <silent> <leader>bs :ls<cr>
        "bb -> Zwischen Buffern wechseln
        map <silent> <leader>bb :ls<CR>:b
        "k -> Zeige nächsten Buffer
        nmap <silent> <leader>j :bnext<cr>
        "j -> Zeige vorherigen Buffer
        nmap <silent> <leader>k :bprevious<cr>
        "bn -> Neuen Buffer öffne
        nmap <silent> <leader>bn :enew<cr>
        "bd -> Buffer schließen
        nmap <silent> <leader>bd :bd!<cr>
        "Diverses
        "ev -> Edit .vimrc in neuem Tab
        nmap <silent> <leader>ev :e $MYVIMRC<cr>
        "re -> :reg
        nmap <silent> <leader>re :reg<cr>
        "sr -> search and replace pattern
        noremap <silent> <leader>sr :%s:::g<Left><Left><Left>
        "ma -> :marks
        nmap <silent> <leader>ma :marks<cr>
        " ,/ um Highlight bei Suche zu löschen
        nmap <silent> <leader>/ :nohlsearch<CR>
        "F-Tasten
        "F2 -> Toggle line numbers
        nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>
        "F3 -> Umschalten zwischen Formatoptions automatic
        function ToggleFoA()
          if &fo =~ 'a'
            set fo-=a    
            set fo=t1 
            echo "Auto Aus!"
          else
            set fo+=a
            echo "Auto An!"
          endif
        endfunction

        map <F3> :call ToggleFoA()<CR>
        imap <F3> <Esc> :call ToggleFoA()<CR>i

        command! Ja set fo+=a
        command! Nein set fo=t1
        "F4 -> Python2-Compiler
        "F5 -> Python3-Compiler
        "F6 -> Wörterbuch
        map <F6> :setlocal spell! spelllang=de,en<CR>
        "F7 -> Latex-Befehle automatisch einfüllen
        "F9 -> Autocomplete für Biblatex bei \cite{}
        "jj/jk fur Esc
        inoremap jk <esc>
        inoremap jj <esc>
        " j und k fur gewrappte Zeilen
        nnoremap gj j
        nnoremap gk k
        nnoremap j gj
        nnoremap k gk
       "Pfeiltasten für Fensternavigation
       nnoremap <up> <C-w>k
       nnoremap <down> <C-w>j
       nnoremap <left> <C-w>h
       nnoremap <right> <C-w>l
        "Cut/Copy/Paste mit cvx in GVim -> Strg+xcv
        vmap <C-c> "+yi
        vmap <C-x> "+c
        imap <C-v> <C-r><C-o>+
        "Enter/Shift-Enter für neue Zeile ohne Insert
        nmap <CR> o<Esc>
        nmap <S-CR> O<Esc>
        "zs -> Fold everything except were cursor is
        nnoremap zs zMzv
        "Use Q for formatting the current paragraph (or selection)
        "formats marked in visual mode
        vmap Q gq 
        "format whole paragraph in normal mode
        nmap Q gqap 
        "Use Alt+Q to format paragraph with par
        map <A-q> {v}!par -jw96<CR>
        vmap <A-q> !par -jw96<CR>
        "won't deselect visual selection when moving selected code blocks
        vnoremap < <gv 
        vnoremap > >gv
        "W ist w/ Q ist q
        "cmap W w
        cmap Q q
        "+ als *
        "nnoremap + *
        "Alt+j/k -> Jump to the next or previous line with same or lower indentation
                " exclusive (bool): true: Motion is exclusive
                " false: Motion is inclusive
                " fwd (bool): true: Go to next line
                " false: Go to previous line
                " lowerlevel (bool): true: Go to line with lower indentation level
                " false: Go to line with the same indentation level
                " skipblanks (bool): true: Skip blank lines
                " false: Don't skip blank lines
                function! NextIndent(exclusive, fwd, lowerlevel, skipblanks)
                  let line = line('.')
                  let column = col('.')
                  let lastline = line('$')
                  let indent = indent(line)
                  let stepvalue = a:fwd ? 1 : -1
                  while (line > 0 && line <= lastline)
                    let line = line + stepvalue
                    if ( ! a:lowerlevel && indent(line) == indent ||
                          \ a:lowerlevel && indent(line) < indent)
                      if (! a:skipblanks || strlen(getline(line)) > 0)
                        if (a:exclusive)
                          let line = line - stepvalue
                        endif
                        exe line
                        exe "normal " column . "|"
                        return
                      endif
                    endif
                  endwhile
                endfunction
        nnoremap <silent> <M-k> :call NextIndent(0, 0, 0, 1)<CR>
        nnoremap <silent> <M-j> :call NextIndent(0, 1, 0, 1)<CR>
        nnoremap <silent> [L :call NextIndent(0, 0, 1, 1)<CR>
        nnoremap <silent> ]L :call NextIndent(0, 1, 1, 1)<CR>
        vnoremap <silent> [l <Esc>:call NextIndent(0, 0, 0, 1)<CR>m'gv''
        vnoremap <silent> ]l <Esc>:call NextIndent(0, 1, 0, 1)<CR>m'gv''
        vnoremap <silent> [L <Esc>:call NextIndent(0, 0, 1, 1)<CR>m'gv''
        vnoremap <silent> ]L <Esc>:call NextIndent(0, 1, 1, 1)<CR>m'gv''
        onoremap <silent> [l :call NextIndent(0, 0, 0, 1)<CR>
        onoremap <silent> ]l :call NextIndent(0, 1, 0, 1)<CR>
        onoremap <silent> [L :call NextIndent(1, 0, 1, 1)<CR>
        onoremap <silent> ]L :call NextIndent(1, 1, 1, 1)<CR>

" Custom Macros
        "@z: Für Kobo-Annotations
        let @r='?<annotation>V/<\/annotation>d'
        let @t='/end="v$di?end="Pgjdd'
        let @s='/<annotation>/<text>f>lv/<\/text>hd?<\/text>ni p'
        let @u='/<text>dd/<annotation>V/<\/annotation>d'
        let @k='@t@s@u'
        let @z='gg/seiteWvt<"aygg/a--@rgg/seite a/<\/annotp@k'
        "@m: Für Marginalnote (Lat. Text)
        let @m='veyea\mynote{\textbf{}\textit{}: }jk'
        let @x='/\. ajk@x'
        let @y='/\; ajk@y'

"Custom Commands
        ":RemoveMultipleBlankLines
        command RemoveMultipleBlankLines %s/^\(\s*\n\)\+/\r
        ":w!! -> um schreibgeschütze Datei mit sudo zu speichern
        cmap w!! w !sudo tee % >/dev/null
        ":Pydir -> Change Directory ~/lib/python
        command Pydir cd ~/lib/python/ | :NERDTree
        " :Qwertz/:Neo2 remappings
        command Neo2 noremap s h  |
                        \ noremap n gj |
                        \ noremap r gk |
                        \ noremap t l |
                        " kill
                        \ noremap k s |
                        " jump
                        \ noremap j n |
                        " hide
                        \ noremap h r |
                        " lookup
                        \ noremap l t |
        command Qwertz noremap s h  |
                        \ noremap gj n |
                        \ noremap gk r |
                        \ noremap l t |
                        " kill
                        \ noremap s k |
                        " jump
                        \ noremap n j |
                        " hide
                        \ noremap r h |
                        " lookup
                        \ noremap t l |
        ":Prose/:Code -> Umschalten Prosa und Code
        command! Prose silent! inoremap <buffer> . .<C-G>u|
                     \ silent! inoremap <buffer> ! !<C-G>u|
                     \ silent! inoremap <buffer> ? ?<C-G>u|
                     \ setlocal nolist wrap
                     \     tw=96 fo=t1 nosmartindent linebreak nu|
                     \ silent! colorscheme solarized |
                     \ set background=light |
                     \ set guifont=Monospace\ 10 |
                     \ highlight NonText cterm=none ctermfg=0 guifg=#dc322f
                     "\ augroup PROSE|
                     "\   autocmd InsertEnter <buffer> set fo+=a|
                     "\   autocmd InsertLeave <buffer> set fo-=a|
                     "\ augroup END

        command! Code silent! iunmap <buffer> .|
                    \ silent! iunmap <buffer> !|
                    \ silent! iunmap <buffer> ?|
                    \ setlocal nospell list wrap
                    \     tw=96 fo=cqr1 smartindent nolinebreak nu|
                    \ silent! colorscheme solarized |
                    \ set background=dark |
                    \ set guifont=Monospace\ 10 |
                    \ set listchars=tab:>.,trail:.,nbsp:. | ",eol:$,extends:$| "". bei Tab
                    \ autocmd filetype html,xml set listchars-=tab:>. | ""keine . bei Tab
                    \ nnoremap j gj |
                    \ nnoremap k gk |
                    \ silent! autocmd! PROSE * <buffer>

"Plugin Settings
"Pathogen
        silent! call pathogen#infect()
"TaskList
        let g:tlTokenList = ['TODO','todo', 'XXX', 'xxx', '???'] "Tastlist Suchbefehle
"Nerdtree
        let NERDTreeQuitOnOpen = 1 "Close Nerdtree wenn man Datei öffnet
"UltiSnips
        let g:UltiSnipsEditSplit = "vertical"                             "Open edit Window vertically
        let g:UltiSnipsSnippetsDir = "~/dotfiles/vim/ultisnips-snippets/" "UltiSnips Directory
        let g:UltiSnipsSnippetDirectories = ["ultisnips-snippets"]
        let g:UltiSnipsExpandTrigger = '<C-u>'                            "Key for UltiSnips Trigger
"Jedi Vim
        let g:jedi#popup_on_dot = 1 "Autocompletion when typing
        let g:jedi#auto_initialization = 1 "Jedi-Vim is auto inizialized
        let g:jedi#auto_vim_configuration = 1
        let g:jedi#use_tabs_not_buffers = 0 "Use buffers
        let g:jedi#completions_command = "<C-Space>" "Use Strg-Space to autocomplete
        let g:jedi#documentation_command = "D" "Use D over definition to show doc
        let g:jedi#goto_assignments_command = "<leader>g"
        let g:jedi#goto_definitions_command = "<leader>d"
        let g:jedi#usages_command = "<leader>n"
        let g:jedi#rename_command = "<leader>r"
"Python-Mode
        let g:pymode_lint_checker = "pyflakes"
        let g:pymode_lint_cwindow = 0           " Auto open cwindow if errors be finded
        let g:pymode_rope = 1                   "Turn off rope plugin
        let g:pymode_rope_autocomplete_map = '' "Use jedi for autocompletion
        let g:pymode_rope_show_doc_bind = ''    "Use jedi for documentation
        let g:pymode_rope_goto_definition_bind = '' "Use jedi to go to Def
"Supertab
        let g:SuperTabDefaultCompletionType = "context"
        let g:SuperTabContextTextOmniPrecedence = ['&omnifunc', '&completefunc']
"FoldDigest
        let folddigest_size = 20
"Conqe-Shell
        "Copy python code to Shell (Open with :ConqueTermSplit python) with ,mp, change to code
        "with ,np  
        imap <silent> <leader>cs <Esc>Vy<C-w><C-w>p
        nmap <silent> <leader>cs Vy<C-w><C-w>p
        vmap <silent> <leader>cs y<C-w><C-w>p
        imap <silent> <leader>cn <Esc><C-w><S-w>']0j
        nmap <silent> <leader>cn <C-w><S-w>']0j
"Airline
        let g:airline#extensions#tabline#enabled = 1          "Enable top list of buffers
        let g:airline#extensions#tabline#fnamemod = ':t'      "Show just filename of buffers
        let g:airline#extensions#tabline#buffer_idx_mode = 1  "Show buffer number
        let g:airline#extensions#tabline#buffer_min_count = 2 "Open buffer list when 2 b exist
                nmap <leader>1 <Plug>AirlineSelectTab1
                nmap <leader>2 <Plug>AirlineSelectTab2
                nmap <leader>3 <Plug>AirlineSelectTab3
                nmap <leader>4 <Plug>AirlineSelectTab4
                nmap <leader>5 <Plug>AirlineSelectTab5
                nmap <leader>6 <Plug>AirlineSelectTab6
                nmap <leader>7 <Plug>AirlineSelectTab7
                nmap <leader>8 <Plug>AirlineSelectTab8
                nmap <leader>9 <Plug>AirlineSelectTab9
"Rainbow
        let g:rainbow_active = 0
        let g:rainbow_conf = {
        \   'guifgs': ['royalblue3', 'darkorange3', 'seagreen3', 'firebrick'],
        \   'ctermfgs': ['lightblue', 'lightyellow', 'lightcyan', 'lightmagenta'],
        \   'operators': '_,_',
        \   'parentheses': ['start=/(/ end=/)/ fold', 'start=/\[/ end=/\]/ fold', 'start=/{/ end=/}/ fold'],
        \   'separately': {
        \       '*': {},
        \       'tex': {
        \           'parentheses': ['start=/(/ end=/)/', 'start=/\[/ end=/\]/'],
        \       },
        \       'lisp': {
        \           'guifgs': ['royalblue3', 'darkorange3', 'seagreen3', 'firebrick', 'darkorchid3'],
        \       },
        \       'vim': {
        \           'parentheses': ['start=/(/ end=/)/', 'start=/\[/ end=/\]/', 'start=/{/ end=/}/ fold', 'start=/(/ end=/)/ containedin=vimfuncbody', 'start=/\[/ end=/\]/ containedin=vimfuncbody', 'start=/{/ end=/}/ fold containedin=vimfuncbody'],
        \       },
        \       'html': {
        \           'parentheses': ['start=/\v\<((area|base|br|col|embed|hr|img|input|keygen|link|menuitem|meta|param|source|track|wbr)[ >])@!\z([-_:a-za-z0-9]+)(\s+[-_:a-za-z0-9]+(\=("[^"]*"|'."'".'[^'."'".']*'."'".'|[^ '."'".'"><=`]*))?)*\>/ end=#</\z1># fold'],
        \       },
        \       'css': 0,
        \   }
        \}

"Filetypes
"Python
        ""http://dancingpenguinsoflight.com/2009/02/python-and-vim-make-your-own-ide/
        map <f4> :w\|!python2 %
        map <f5> :w\|!python3 %
        autocmd FileType python Code "Starte Python automatisch in Code
        autocmd FileType python RainbowToggle "Starte mit Rainbow Parentheses
        au FileType python setlocal tabstop=8 expandtab shiftwidth=4 softtabstop=4 nolinebreak
        autocmd FileType python highlight SpellBad term=underline gui=bold guisp=Orange guifg=red
        autocmd FileType python set complete+=k~/.vim/syntax/python.vim isk+=.,( "~/.vim/syntax
        set number "Turn on line numbers
        let g:SuperTabDefaultCompletionType = "context"
"Sage
        "To get Vim to use Python syntax highlighting, indentation, and so on for .sage files
        augroup filetypedetect
          au! BufRead,BufNewFile *.sage,*.spyx,*.pyx setfiletype python
        augroup END
"Shell-Script
        autocmd FileType sh Code
        autocmd FileType sh RainbowToggle "Starte mit Rainbow Parentheses
        au FileType tabstop=8 expandtab shiftwidth=4 softtabstop=4 nolinebreak
"C
        autocmd FileType c Code
        autocmd FileType c RainbowToggle "Starte mit Rainbow Parentheses
"Latex/Vim-Latex
        let g:tex_flavor="latex"
        autocmd FileType tex Prose "Starte LaTex automisch in Prosa
        autocmd FileType tex RainbowToggle "Starte mit Rainbow Parentheses
        au Filetype tex setlocal tabstop=2 expandtab shiftwidth=2 softtabstop=2 linebreak
        let g:Tex_BIBINPUTS="$PWD/*.bib" "F9->Bibtex autocomplete
        let g:Tex_ViewRule_dvi = "xdvi" "Open Dvi with xdvi
        imap <C-g> <Plug>IMAP_JumpForward
        nmap <C-g> <Plug>IMAP_JumpForward
        "Fold-Options verändert in dotfiles/vim/bundle/latex-suite/ftplugin/latex-suite/folding.vim, geschützt mit chattr +i
        ""let g:Tex_FoldedSections = 'section,%%fakesection,%%fakesubsection'
        ""let g:Tex_FoldedEnvironments = "abstract"
         " redef C-j to C-g
"Html
        autocmd FileType html Code
        autocmd FileType html RainbowToggle "Starte mit Rainbow Parentheses
"Markdown
        autocmd FileType markdown Prose
"Xml
        autocmd FileType xml Code
"Mail
        autocmd FileType mail setlocal fo+=aw
        autocmd FileType mail set spell
"Arduino Ino
        au BufRead,BufNewFile *.ino,*.pde :cd.. "One directory down to compile
        "Compile and upload
        map <leader>ac :<Esc>:w<CR>:!clear<CR>:!ino build --cxxflags=-I$PWD/src<CR>:!ino upload<CR>: <Ins> <CR>
        "Show Serial Monitor
        map <leader>as :<Esc>:w<CR>:!clear<CR>:!ino serial -b 9600<CR> 
