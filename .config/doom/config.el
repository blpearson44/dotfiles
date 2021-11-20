;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-
(setq user-full-name "Ben Pearson")
(setq user-mail-address "blpearson44@icloud.com")
(setq doom-font (font-spec :family "Fira Code" :size 20))
(setq doom-theme 'doom-one)

(setq org-directory "~/Org/")
(setq org-roam-directory "~/Org/Spiderverse")
(setq display-line-numbers-type t)


;; Projectile
(setq projectile-project-search-path '("~/Projects/"))
(setq projectile-auto-discover t)


;; Org
;; Change heading fonts
(custom-set-faces
  '(org-level-1 ((t (:inherit outline-1 :height 1.2))))
  '(org-level-2 ((t (:inherit outline-2 :height 1.0))))
  '(org-level-3 ((t (:inherit outline-3 :height 1.0))))
  '(org-level-4 ((t (:inherit outline-4 :height 1.0))))
  '(org-level-5 ((t (:inherit outline-5 :height 1.0))))
)
(use-package! websocket
    :after org-roam)

(use-package! org-roam-ui
    :after org-roam ;; or :after org
;;         normally we'd recommend hooking orui after org-roam, but since org-roam does not have
;;         a hookable mode anymore, you're advised to pick something yourself
;;         if you don't care about startup time, use
;;  :hook (after-init . org-roam-ui-mode)
    :config
    (setq org-roam-ui-sync-theme t
          org-roam-ui-follow t
          org-roam-ui-update-on-save t
          org-roam-ui-open-on-start t))


;; Doom Dashboard
(defun +fl/cowsay-fortune-banner ()
  (mapc (lambda (line)
          (insert (propertize (+doom-dashboard--center +doom-dashboard--width line)
                              'face 'doom-dashboard-banner) " ")
          (insert "\n"))
        (split-string (with-output-to-string
                        (call-process-shell-command "fortune -s humorists drugs computers cookie fortunes | cowsay" nil standard-output))
                      "\n" t)))

(setq +doom-dashboard-ascii-banner-fn #'+fl/cowsay-fortune-banner)



;; Org-bullets
(use-package! org-bullets)
(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))


;; Prettify-Symbols-Mode
;; ligatures
;; unless noted otherwise, commented ligatures show wrong symbols and as such are not used
(defun my/pretty-symbols ()
  (setq prettify-symbols-alist
  '(("www" 160 #1=(Br . Bl) 160 #1# 57600)
    ("**" 160 #1# 57601)
    ("***" 160 #1# 160 #1# 57602)
    ("**/" 160 #1# 160 #1# 57603)
    ("*>" 160 #1# 57604)
    ("*/" 160 #1# 57605)
    ("\\\\" 160 #1# 57606)
    ("\\\\\\" 160 #1# 160 #1# 57607)
    ("{-" 160 #1# 57608)
    ;; ("[]" 160 #1# 57609) This one just makes it annoying to enter things into brackets
    ("::" 160 #1# 57610)
    (":::" 160 #1# 160 #1# 57611)
    (":=" 160 #1# 57612)
    ("!!" 160 #1# 57613)
    ("!=" 160 #1# 57614)
    ("!==" 160 #1# 160 #1# 57615)
    ("-}" 160 #1# 57616)
    ("--" 160 #1# 57617)
    ("---" 160 #1# 160 #1# 57618)
    ("-->" 160 #1# 160 #1# 57619)
    ("->" 160 #1# 57620)
    ("->>" 160 #1# 160 #1# 57621)
    ("-<" 160 #1# 57622)
    ("-<<" 160 #1# 160 #1# 57623)
    ("-~" 160 #1# 57624)
    ("#{" 160 #1# 57625)
    ("#[" 160 #1# 57626)
    ("##" 160 #1# 57627)
    ("###" 160 #1# 160 #1# 57628)
    ("####" 160 #1# 160 #1# 160 #1# 57629)
    ("#(" 160 #1# 57630)
    ("#?" 160 #1# 57631)
    ("#_" 160 #1# 57632)
    ("#_(" 160 #1# 160 #1# 57633)
    (".-" 160 #1# 57634)
    (".=" 160 #1# 57635)
    (".." 160 #1# 57636)
    ("..<" 160 #1# 160 #1# 57637)
    ("..." 160 #1# 160 #1# 57638)
    ("?=" 160 #1# 57639)
    ("??" 160 #1# 57640)
    (";;" 160 #1# 57641)
    ("/*" 160 #1# 57642)
    ("/**" 160 #1# 160 #1# 57643)
    ("/=" 160 #1# 57644)
    ("/==" 160 #1# 160 #1# 57645)
    ("/>" 160 #1# 57646)
    ("//" 160 #1# 57647)
    ("///" 160 #1# 160 #1# 57648)
    ("&&" 160 #1# 57649)
    ("||" 160 #1# 57650)
    ("||=" 160 #1# 160 #1# 57651)
    ("|=" 160 #1# 57652)
    ("|>" 160 #1# 57653)
    ("^=" 160 #1# 57654)
    ("$>" 160 #1# 57655)
    ("++" 160 #1# 57656)
    ("+++" 160 #1# 160 #1# 57657)
    ("+>" 160 #1# 57658)
    ("=:=" 160 #1# 160 #1# 57659)
    ("==" 160 #1# 57660)
    ("===" 160 #1# 160 #1# 57661)
    ("==>" 160 #1# 160 #1# 57662)
    ("=>" 160 #1# 57663)
    ("=>>" 160 #1# 160 #1# 57664)
    ;; ("=<" 160 #1# 57665)=<
    ("=<<" 160 #1# 160 #1# 57666)
    ("=/=" 160 #1# 160 #1# 57667)
    (">-" 160 #1# 57668)
    ;; (">=" 160 #1# 57669) character does not display properly (despite being matched properly)
    ;; (">=>" 160 #1# 160 #1# 57670)>=>
    (">>" 160 #1# 57671)
    ;; (">>-" 160 #1# 160 #1# 57672)>>-
    ;; (">>=" 160 #1# 160 #1# 57673)>>=
    ;; (">>>" 160 #1# 160 #1# 57674)>>>
    ;; ("<*" 160 #1# 57675)<*
    ;; ("<*>" 160 #1# 160 #1# 57676)<*>
    ;; ("<|" 160 #1# 57677)<|
    ;; ("<|>" 160 #1# 160 #1# 57678)<|>
    ;; ("<$" 160 #1# 57679)<$
    ;; ("<$>" 160 #1# 160 #1# 57680)<$>
    ;; ("<!--" 160 #1# 160 #1# 160 #1# 57681)<!--
    ;; ("<-" 160 #1# 57682)<-
    ("<--" 160 #1# 160 #1# 57683)
    ;; ("<->" 160 #1# 160 #1# 57684)<->
    ;; ("<+" 160 #1# 57685)<+
    ;; ("<+>" 160 #1# 160 #1# 57686)<+>
    ;; ("<=" 160 #1# 57665) character displays properly but >= does not so both are disabled
    ;; ("<==" 160 #1# 160 #1# 57688)<==
    ;; ("<=>" 160 #1# 160 #1# 57689)<=>
    ;; ("<=<" 160 #1# 160 #1# 57690)<=<
    ;; ("<>" 160 #1# 57691)<>
    ("<<" 160 #1# 57692)
    ;; ("<<-" 160 #1# 160 #1# 57693)<<-
    ;; ("<<=" 160 #1# 160 #1# 57694)<<=
    ;; ("<<<" 160 #1# 160 #1# 57695)<<<
    ;; ("<~" 160 #1# 57696)<~
    ;; ("<~~" 160 #1# 160 #1# 57697)<~~
    ;; ("</" 160 #1# 57698)</
    ;; ("</>" 160 #1# 160 #1# 57699)</>
    ;; ("~@" 160 #1# 57700)~@
    ;; ("~-" 160 #1# 57701)~-
    ;; ("~=" 160 #1# 57702)~=
    ;; ("~>" 160 #1# 57703)~>
    ;; ("~~" 160 #1# 57704)~~
    ;; ("~~>" 160 #1# 160 #1# 57705)~~>
    ;; ("%%" 160 #1# 57706)%%
    ("x" "x")
    (":" ":")
    ("+" 57710)
    ("*" 57711)
    )))
(add-hook 'prog-mode-hook 'my/pretty-symbols)
(add-hook 'org-mode-hook 'my/pretty-symbols)


;; Indent Guides
(setq highlight-indent-guides-bitmap-function 'highlight-indent-guides--bitmap-line)
(setq highlight-indent-guides-responsive 'top)
(setq highlight-indent-guides-method 'bitmap)


;; Whitespace
(defun my/whitespace ()
  (setq
   whitespace-style '(face tabs tab-mark spaces space-mark trailing lines-tail newline newline-mark)
   whitespace-display-mappings '(
                                 (space-mark   ?\     [?\u00B7]     [?.])
                                 (space-mark   ?\xA0  [?\u00A4]     [?_])
                                 (newline-mark ?\n    [?¬ ?\n])
                                 (tab-mark     ?\t    [?\u00BB ?\t] [?\\ ?\t]))))
(after! whitespace
  (add-hook 'whitespace-mode-hook 'my/whitespace))


;; Keymappings
;; Global
;; Whitespace
(map! :leader
      :desc "Enable whitespace-mode" "W" #'whitespace-mode)
;; Dired
(map! :leader
      (:prefix ("d" . "dired")
       :desc "Dired jump to current" "j" #'dired-jump)
      (:after dired
       (:map dired-mode-map
        :desc "Peep-dired image previews" "d p" #'peep-dired
        :desc "Dired view file" "d v" #'dired-view-file)))
;; Registers
(map! :leader
      (:prefix ("r" . "registers")
       :desc "Copy to register" "c" #'copy-to-register
       :desc "Frameset to register" "f" #'frameset-to-register
       :desc "Insert contents of register" "i" #'insert-register
       :desc "Jump to register" "j" #'jump-to-register
       :desc "List registers" "l" #'list-registers
       :desc "Number to register" "n" #'number-to-register
       :desc "Interactively choose a register" "r" #'counsel-register
       :desc "View a register" "v" #'view-register
       :desc "Window configuration to register" "w" #'window-configuration-to-register
       :desc "Increment register" "+" #'increment-register
       :desc "Point to register" "SPC" #'point-to-register))
;; Dired-mode
;; Make 'h' and 'l' go back and forward in dired. Much faster to navigate the directory structure!
(evil-define-key 'normal dired-mode-map
  (kbd "M-RET") 'dired-display-file
  (kbd "h") 'dired-up-directory
  (kbd "l") 'dired-open-file ; use dired-find-file instead of dired-open.
  (kbd "m") 'dired-mark
  (kbd "t") 'dired-toggle-marks
  (kbd "u") 'dired-unmark
  (kbd "C") 'dired-do-copy
  (kbd "D") 'dired-do-delete
  (kbd "J") 'dired-goto-file
  (kbd "M") 'dired-chmod
  (kbd "O") 'dired-chown
  (kbd "P") 'dired-do-print
  (kbd "R") 'dired-rename
  (kbd "T") 'dired-do-touch
  (kbd "Y") 'dired-copy-filenamecopy-filename-as-kill ; copies filename to kill ring.
  (kbd "+") 'dired-create-directory
  (kbd "-") 'dired-up-directory
  (kbd "% l") 'dired-downcase
  (kbd "% u") 'dired-upcase
  (kbd "; d") 'epa-dired-do-decrypt
  (kbd "; e") 'epa-dired-do-encrypt)
;; If peep-dired is enabled, you will get image previews as you go up/down with 'j' and 'k'
(evil-define-key 'normal peep-dired-mode-map
  (kbd "j") 'peep-dired-next-file
  (kbd "k") 'peep-dired-prev-file)
(add-hook 'peep-dired-hook 'evil-normalize-keymaps)
;; Get file icons in dired
(add-hook 'dired-mode-hook 'all-the-icons-dired-mode)
;; With dired-open plugin, you can launch external programs for certain extensions
;; For example, I set all .png files to open in 'sxiv' and all .mp4 files to open in 'mpv'
(setq dired-open-extensions '(("gif" . "sxiv")
                              ("jpg" . "sxiv")
                              ("png" . "sxiv")
                              ("mkv" . "mpv")
                              ("mp4" . "mpv")))
