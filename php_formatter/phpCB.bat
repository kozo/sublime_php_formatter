phpCB.exe --space-after-if ^
	--space-after-switch ^
	--space-after-while ^
	--space-before-start-angle-bracket ^
	--space-after-end-angle-bracket ^
	--one-true-brace-function-declaration ^
	--glue-amperscore ^
	--change-shell-comment-to-double-slashes-comment ^
	--force-large-php-code-tag ^
	--force-true-false-null-contant-lowercase ^
	--align-equal-statements ^
	--equal-align-position 50 ^
	--padding-char-count 4 ^
	--optimize-eol ^
	--glue-arrow ^
	--comment-rendering-style PEAR ^
	"%1" > "%TEMP%\phpcb.php"
rem move /Y "%TEMP%\phpcb.php" "%1"
rem PAUSE
