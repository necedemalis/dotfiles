".vimrc
" The ArchLinux global vimrc - setting only a few sane defaults
"
" Maintainer:      Tobias Kieslich [tobias funnychar archlinux dot org]
"
" NEVER EDIT THIS FILE, IT'S OVERWRITTEN UPON UPGRADES, GLOBAL CONFIGURATION
" SHALL BE DONE IN /etc/vimrc, USER SPECIFIC CONFIGURATION IN ~/.vimrc

" Normally we use vim-extensions. If you want true vi-compatibility
" remove change the following statements
set nocompatible                " Use Vim defaults instead of 100% vi compatibility
set backspace=indent,eol,start  " more powerful backspacing

" Now we set some defaults for the editor
set history=50                  " keep 50 lines of command line history
set ruler                       " show

" Suffixes that get lower priority when doing tab completion for filenames.
" These are files we are not likely to want to edit or read.
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc

if has('gui_running')
  " Make shift-insert work like in Xterm
  map <S-Insert> <MiddleMouse>
  map! <S-Insert> <MiddleMouse>
endif


""""""""""
""Custom""
""""""""""
        let mapleader="," ", statt \ als leader key
        colorscheme ChocolateLiquor
        "Detect file types
        filetype on
        filetype plugin on
        filetype plugin indent on
        syntax on

"Basic Settings
        "set 
        set hls ic is "Search: Highlight, ignore case, show
        set smartcase "ignore case if search pattern is all lowercase,
        set nocp "nocompatible
        set et "expandtab
        set smarttab "Insert tabs at the start of a line
        set tw=96
        set showbreak=>>>>
        set wildignore=*.swp,*.bak,*.pyc,*.class "ignore some file extensions when completing names by pressing Tab,
        set visualbell " Visuelles Piepen 
        set noerrorbells " don't beep
        set hidden  "zwischen Buffern wechseln ohne speichern zu mÃ¼ssen
        set autowrite "speichter Datei automatisch beim wechseln
        set guioptions-=T "Versteckt GUI-Toolbar
        set guioptions-=m "Versteckt GUI-Toolbar
        set autoindent "Copy indent from current line when starting a new line 
        set go+=c "No Popup-Dialogs
        set shortmess+=I "Keine Startup-Message
        "Pathogen
        call pathogen#infect()
        "Save/Load manual made Folds
        au BufWinLeave * silent! mkview
        au BufWinEnter * silent! loadview
        "Backup
        set backup
        set noswapfile
        set backupdir=~/.vim/.backup,/tmp
        set directory=~/.vim/.backup,/tmp
        set writebackup
        "TaskList Suchbefehle
        let g:tlTokenList = ['TODO','todo', 'XXX', 'xxx', '???']
        "Close Nerdtree wenn man Datei Ã¶ffnet
        let NERDTreeQuitOnOpen = 1 
        " Source .vimrc file after saving
        "if has("autocmd")
        " augroup myvimrchooks
        "  au!
        "  autocmd bufwritepost .vimrc source ~/.vimrc
        " augroup END
        "endif

" Neo2 remappings
        noremap s h
        noremap n gj
        noremap r gk
        noremap t l
        " kill
        noremap k s
        " jump
        noremap j n
        " hide
        noremap h r
        " lookup
        noremap l t

" Custom Keymapping
        "Leader Keymapping
        "vr -> Toggle Vimroom
        nmap <leader>vr :colorscheme iawriter\|:VimroomToggle<cr>   
        "fd -> FoldDigest()
        nmap <leader>fd :call FoldDigest ()<cr>
        "tl -> :TaskList
        map <leader>tl :TaskList<cr> 
        "nt -> :NerdTree
        nmap <leader>nt :NERDTree<cr>
        "pr -> :Prose
        nmap <silent> <leader>pr :Prose<cr>
        "co -> :Code
        nmap <silent> <leader>co :Code<cr>
        "bs -> zeigt Buffer an
        nmap <leader>bs :ls<cr>
        "bb -> Zwischen Buffern wechseln
        map <leader>bb :ls<CR>:b
        "bn -> Zeige nächsten Buffer
        nmap <leader>bn :b#<cr>
        "bd -> Buffer schlieÃen
        nmap <leader>bd :bd<cr>
        "ev -> Edit .vimrc in neuem Tab
        nmap <leader>ev :e $MYVIMRC<cr>
        "re -> :reg
        nmap <leader>re :reg<cr>
        "sr -> search and replace pattern
        noremap <leader>sr :%s:::g<Left><Left><Left>
        "ma -> :marks
        nmap <leader>ma :marks<cr>
        "pp -> Compile Python
        map <leader>pp :w\|!python3 %
        "Strg+xcv -> Cut/Copy/Paste mit cvx in GVim
        vmap <C-c> "+yi
        vmap <C-x> "+c
        "vmap <C-v> c<ESC>"+p
        imap <C-v> <C-r><C-o>+
        " Use Q for formatting the current paragraph (or selection)
        vmap Q gq
        nmap Q gqap
        "jj/jk fur Esc
        inoremap jk <esc>
        inoremap jj <esc>
        " j und k fur gewrappte Zeilen
        "nnoremap j gj
        "nnoremap k gk
        "W ist w/ Q ist q
        cmap W w
        cmap Q q
        " ,/ um Highlight bei Suche zu lÃ¶schen
        nmap <silent> ,/ :nohlsearch<CR>
        "Pfeiltasen deaktivieren
       "inoremap <up> <nop>
       "inoremap <down> <nop>
       "inoremap <left> <nop>
       "inoremap <right> <nop>
       "Pfeiltasten fÃ¼r Fensternavigation
       " let g:C_Ctrl_j   = 'off'
       " let g:BASH_Ctrl_j = 'off'
       "nnoremap <C-h> <C-w>h
       "nnoremap <C-j> <C-w>j
       "nnoremap <C-k> <C-w>k
       "nnoremap <C-l> <C-w>l
       nnoremap <up> <C-w>k
       nnoremap <down> <C-w>j
       nnoremap <left> <C-w>h
       nnoremap <right> <C-w>l
        "+ als *
        nnoremap + *
        "Strg+C/Strg+Leertase -> Omnicompletion 
        ""imap <C-c> <C-x><C-o>
        ""imap <C-Space> <C-x><C-o>
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
        "F4 -> DistractionFreeWriting-Scheme (s. Plugin)
        "F5 -> Python-Compiler
        "F6 -> WÃ¶rterbuch
        map <F6> :setlocal spell! spelllang=de,en<CR>
        "F7 -> Latex-Befehle automatisch einfÃ¼llen
        "F8 -> Fold Digest
        "map <F8> :call FoldDigest ()<CR>
        "F9 -> Autocomplete fÃ¼r Biblatex bei \cite{}

" Custom Macros
        "Für Kobo-Annotations (r=Delete zweiten Teil, t=fÃ¼ge zweiten Teil zu ersten Teil),
        "schauen ob </text am zeilenanfang
        let @r='?<annotation>V/<\/annotation>d'
        let @t='/end="v$di?end="Pnndd'
        let @s='/<text>f>tv/<\/text>sd?<\/text>ji p'
        let @u='/<text>dd/<annotation>V/<\/annotation>d'
        let @k='@t/<annot@s@u'
        let @z='gg/seiteWvtt"aygg/a--@rgg/seite a/<\/annotýLpýLýLýLýLýL@k'

"Custom Commands
        "Remove Multiple Blank Lines
        command RemoveMultipleBlankLines %s/^\(\s*\n\)\+/\r
        ":w!! um schreibgeschÃ¼tze Datei mit sudo zu speichern
        cmap w!! w !sudo tee % >/dev/null
        "Pydir -> Change Directory ~/lib/python
        command Pydir cd ~/lib/python/ | :NERDTree
        "Dip/Dipdir -> Change Directory ~/lib/python
        command Dipdir cd ~/Dropbox/Diplomarbeit/Diplomarbeit/ | :NERDTree
        command Dip :e ~/Dropbox/Diplomarbeit/Diplomarbeit/Diplomarbeit.tex | cd ~/Dropbox/Diplomarbeit/
        "Umschalten Prosa und Code
        command! Prose colorscheme ChocolateLiquor |
                     \ inoremap <buffer> . .<C-G>u|
                     \ inoremap <buffer> ! !<C-G>u|
                     \ inoremap <buffer> ? ?<C-G>u|
                     \ setlocal 
                     \ nolist wrap tw=96 fo=t1 nosmartindent linebreak nu|
                     \ set background=light |
                     \ colorscheme solarized |
                     "\ augroup PROSE|
                     "\   autocmd InsertEnter <buffer> set fo+=a|
                     "\   autocmd InsertLeave <buffer> set fo-=a|
                     "\ augroup END

        command! Code silent! iunmap <buffer> .|
                    \ silent! iunmap <buffer> !|
                    \ silent! iunmap <buffer> ?|
                    \ setlocal nospell list wrap
                    \     tw=96 fo=cqr1 smartindent nolinebreak nu|
                    \ set background=dark |
                    \ colorscheme solarized |
                    \ set listchars=tab:>.,trail:.,extends:$,nbsp:. | "". bei Tab
                    \ autocmd filetype html,xml set listchars-=tab:>. | ""keine . bei Tab   
                    \ nnoremap j gj |
                    \ nnoremap k gk |
                    \ silent! autocmd! PROSE * <buffer>

"Python"
        ""http://dancingpenguinsoflight.com/2009/02/python-and-vim-make-your-own-ide/
        map <f5> :w\|!python3 %
        au FileType python setlocal tabstop=8 expandtab shiftwidth=4 softtabstop=4
        "Turn on line numbers:
        set number
        "~/.vim/syntax
        autocmd FileType python set complete+=k~/.vim/syntax/python.vim isk+=.,(
        "Code Omnicompletion
        """autocmd FileType python set omnifunc=pythoncomplete#Complete
        let g:SuperTabDefaultCompletionType = "context"
        let g:jedi#popup_on_dot = 0
        let g:jedi#auto_initialization = 1
        let g:jedi#auto_vim_configuration = 1
        "Starte Python automatisch in Code
        autocmd FileType python Code
        "Wie Errors markieren durch Pyflakes (gui=underline zum unterstreichen)
        autocmd FileType python highlight SpellBad term=underline gui=bold guisp=Orange guifg=red
        "Pydiction
        let g:pydiction_location = '/home/joecool/.vim/pydiction/pydiction-1.2/complete-dict'

"Vim-Latex"
        let g:tex_flavor="latex"
        "F9->Bibtex autocomplete
        let g:Tex_BIBINPUTS="$PWD/*.bib"
        "Starte LaTex automisch in Prosa
        autocmd FileType tex Prose 

"Filetypes
        "Markdown
        autocmd FileType markdown Prose 
        "Shell-Script
        autocmd FileType sh Code 
