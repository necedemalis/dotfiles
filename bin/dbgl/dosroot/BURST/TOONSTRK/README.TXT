-------------------------------------------------------------------------------
                                 Toonstruck
               (c)1996 Burst, A Division of Virgin Interactive
-------------------------------------------------------------------------------

                               Release Notes
                               -------------

Thanks for purchasing Toonstruck!!! These release notes are intended to provide
last minute information regarding ToonStruck. If you are having trouble getting
ToonStruck to run on your system, please read the troubleshooting section below.

------------------------------------------------------------------------------

                             System Requirements
                             -------------------

* Recommended:
    IBM PC Pentium or 100% compatible
    16Mb RAM
    1Mb SVGA Video Card
    4x CD-ROM Drive
    16bit Stereo Sound Card

* Minimum:
    IBM PC 486/66 or 100% compatible
    MS-DOS 5.0 or higher
    30Mb free hard disk space
    Mouse installed
    8Mb RAM
    256k SVGA Video Card ( VLB / PCI )
    2x CD-ROM Drive
    8bit Sound Card

------------------------------------------------------------------------------

                               Installation
                               ------------

* IMPORTANT : Toonstruck is primarily a DOS application. Although we have
              provided support for Windows '95, for optimum performance 
              (especially if your running Toonstruck on a machine with 8
              Megabytes of memory) we advise users to play the game in MS-DOS
              mode. If you are running Windows '95 and wish to run the game
              in MS-DOS mode you can -

              - Select the SHUT DOWN option from the Windows '95 START menu
              - Select the RESTART THE COMPUTER IN MS-DOS MODE Option and 
                click YES.

              Your machine will then shut down and RESTART in MS-DOS mode.

              - Change to the TOONSTRK directory (normally C:\BURST\TOONSTRK)
              - Type TOONSTRK to play

              *** If you have problems running Toonstruck, you may need to
                  have CDROM & MOUSE DRIVERS INSTALLED from the CONFIG.SYS 
                  and AUTOEXEC.BAT files on your system. Please consult your
                  CDROM user manual or vendor for more information 


                            General Installation
                            --------------------

* Windows 95:
    Insert Disc One into your CD-ROM drive.
    After a few seconds a panel should appear
    Click on 'INSTALL' to install the game
    Follow the on-screen instructions.

  Alternative 1:
    Insert CD 1 into your CD-ROM drive.
    From the taskbar select 'START' then 'RUN'
    Click on 'BROWSE' 
    Click on the 'Look In' pull down menu and click on the CD drive icon.
    Click on 'SETUP.EXE' then click on 'OPEN'
    Click on 'OK' to launch the installer
    Follow the on-screen instructions.

  Alternative 2:
    Open up a DOS Prompt and follow the DOS install instructions.

    (Please note that we recommend installing ToonStruck from DOS)

* Windows 3.x:
    Exit to DOS and follow the DOS install instructions.

* DOS:
    Insert CD 1 into your CD-ROM drive.
    Change to your CD drive. eg. D: <enter>
    Type: INSTALL <enter>
    Follow the onscreen instructions.


------------------------------------------------------------------------------

                              Running the Game
                              ----------------

* Windows 95:
    Insert the CD into your CD-ROM drive.
    After a few seconds a panel should appear
    Click on 'PLAY' to launch the game

  Alternative 1:
    From the taskbar select 'START' then 'RUN'.
    Click on 'BROWSE' .
    Click on the 'Look In' pull down menu and click on the drive letter where
    the game installed.
    Click on the directories where the game installed. eg: Click on BURST then
    on TOONSTRK.
    Click on 'TOONSTRK.BAT' then click on 'OPEN'.
    Click on 'OK' to launch the game.

  Alternative 2:
    Open up a DOS Prompt and follow the DOS instructions.

    (Please note that we recommend playing ToonStruck from DOS)

* Windows 3.x:
    Exit to DOS and follow the DOS instructions.

* DOS:
    Insert CD 1 into your CD-ROM drive.
    Change to drive where you installed the game. eg. C: <enter>
    Change to directory where you installed the game. eg. CD \BURST\TOONSTRK
    Type TOONSTRK<enter> to launch the game.


------------------------------------------------------------------------------

                          Troubleshooting Guide
                          ---------------------

This section provides troubleshooting techniques to get ToonStruck running and
to achieve optimum game performance.


Configuration
-------------

If you need to alter the settings for your video card or sound card after
ToonStruck has been installed, change directories to the ToonStruck directory
and run 'SETUP.EXE'.

It is possible to manually configure many of the settings within ToonStruck
in order to overcome a problem. Before trying any of these please read the
'problems & solutions' section below. The use of these switches should not
be necessary if the install program was successful or followed correctly.

Command Line Switches (override 'TOONSTRK.CFG'):
    Usage: TOONSTRK [options]

    -h     Help
    -?     Help
    -u     Disable UniVBE
    -v     Install UniVBE using existing VESA 2.0 Drivers
    -w     Do not sync to monitor refresh
    -6     Force 6-bit DAC palette data
    -p     Do not program the palette (colors)
    -b     Do not double-buffer using video RAM.

Most of the configuration information is obtained from the 'TOONSTRK.CFG'
file. You may change video modes by setting the 'Width' and 'Height' fields
within this file using a text editor. Supported resolution are: 640x400
640x480 320x200.


UniVBE
------

UniVBE is a generic video BIOS extender compatible with VESA 2.0. It enables
quick, linear access to your video card's memory. For ToonStruck to run
optimally either UniVBE has to be installed correctly or you have to be using
a VESA 2.0 video driver supplied by the manufacturer of your video card. 
UniVBE is constantly being revised and upgraded as more and more video cards
become available. If you have problems installing UniVBE, your video card may
not be supported by the version of UniVBE shipped with ToonStruck. 

The following video cards have exhibited some problems running with UniVBE:

        #9 Imagine 128
        Matrox MGA Impression
        Matrox Millenium
        Diamond Stealth 32 PCI (ET4000 chipset)
        Diamond SpeedStar Phantom 32I PCI (ET4000 chipset)
        Diamond Viper VLB
        Kelvin 64 VLB
        ATI 3D Rage/ATI 3D Xpression PCI (Need to set Command Line Switch)
        Hercules Graphite Terminator

For more information look in the SciTech software web site: www.scitechsoft.com. 
To obtain a compatible VESA 2.0 driver contact the manufacturer of your video
card.

Windows '95
-----------

ToonStruck will run in Windows '95 as long as you have more than 8MB of 
memory.  For optimium performance though, we recommend that you reboot 
the system in MS-DOS mode before running the game.  If you do run the 
game from a Windows '95 DOS box (or Prompt), there are a few things that
you should be aware of:

        o If you have trouble configuring your sound card, make sure 
          that the settings in the install program match those being 
          used by Windows '95.  The Windows '95 sound settings are 
          found under 'Control Panel' - 'System' - 'Device Manager' 
          - 'Sound Card'. If you still experience problems after 
          verifying these settings, then it is advisable to boot out 
          to MS-DOS mode and install the game from there.

        o If you are experiencing problems with sound volume or aren't
          hearing any sound, make sure that the volume control slider -
          accessible from the taskbar - is at a reasonable level.  If
          this still doesn't solve the problem, then it is advisable
          to boot out to MS-DOS mode and run the game from there.

        o If you hear an appreciable amount of static or white noise
          during gameplay, then it is advisable to boot out to MS-DOS
          mode and run the game from there.

        o If you are experiencing poor CD performance, make sure that
          Windows '95 has the correct settings for your CD-ROM drive.
          These settings appear under 'Control Panel' - 'System' - 
          'Performance' - 'File System' - 'CD-Rom'.

        o ToonStruck disables your Windows '95 screen saver and all
          shortcut keys (ALT-TAB, ALT-ENTER, etc.).


Problems & Solutions
--------------------

* The install program did not auto-detect the sound card correctly.

    Try manually selecting your sound card settings, if you know them,
    from the sound configuration/configure sound option of the SETUP.EXE
    program.  If you still cannot hear sound you may need to disable
    sound altogether for ToonStruck to run.  In this case, select 
    "No Digital Device" from the manual sound configuration.

    Some or all of the following sound cards may have a problem 
    auto-detecting properly:

        Media Vision Premium 3D SRS
        IBM MWave
        Aztech Sound Galaxy
        Aztech Sound Galaxy NX Pro 16
        Gravis Ultrasound "Classic"

    In all cases, these cards should be manually configured as
    Sound Blaster, with the Port, IRQ and DMA settings appropriate
    to your sound card.

* No sound is heard when 'Test' is selected in the installation program.

    See above.

* The machine locks up with a beeping sound when 'Test' is selected in the
  installation program.

    You are probably running under Windows '95. Shut down and Restart your
    computer in MSDOS mode and try running the setup program. 

* The machine locks-up after displaying the UVBELib banner.

    There is a conflict between UniVBE and one or more programs running
    on your system. Try disabling UniVBE by entering 'TOONSTRK -U' unless
    you have one of the specific components mentioned next. If you have
    'Windows for Workgroups' on your system the program EMM386.EXE could
    be causing the conflict. You should try removing it from the file
    CONFIG.SYS and rebooting your machine.

* The screen goes blank and sound is not heard or stops playing.

    The video setup is causing a conflict with your system. Try disabling
    UniVBE by entering 'TOONSTRK -U'. If this does not work try disabling
    the video card from trying to sync to the monitor by entering
    'TOONSTRK -W' or failing that 'TOONSTRK -U -W'.

* The screen goes blank and sound continues.

    The palette (colors) are not being programmed properly into your video
    card. UniVBE may have detected your video cards DAC incorrectly. Try
    selecting a generic DAC by entering 'UVCONFIG -d7' then running the
    game. Failing that, try disabling UniVBE altogether by entering
    'TOONSTRK -U'.

* The palette (colors) are displayed incorrectly.

    See above.

* The palette (colors) appears too dark.
	
    You may have a 6-bit DAC video card that requires specific palette
    data. Try forcing to a 6-bit palette by entering 'TOONSTRK -6'.

* The sound stutters or 'click' and 'pop' distortion can be heard.

    You may need to alter the rate at which sound gets streamed to your
    sound card or you may need to select mono sound rather than stereo.
    The value 'TimerRate' in the file TOONSTRK.CFG sets the rate at which
    sound gets streamed. The higher the value the clearer the sound but
    the slower the game will run overall. The average setting for mono
    is 60 and for stereo 144. Your machine may need a higher rate so
    adjust it accordingly. If you are running in stereo mode with a rate
    of 150 or more and the sound still breaks up, alter the 'Stereo = 1'
    entry to 'Stereo = 0' and confirm 'TimerRate = 60' to select mono.
    Please note that you may need a higher 'TimerRate' if running from
    Windows '95.

* An error message appears saying 'ToonStruck may play slow or flicker'.

    The optimal video configuration could not be set up on your machine.
    ToonStruck requires a 1Mb video card to run optimally. If you have a 
    1Mb video card and you still get this error message there is a
    possibility that UniVBE did not detect your video card correctly.
    This may be because your video card is too new to be supported by
    the version of UVCONFIG.EXE shipped with ToonStruck. See the section
    on UniVBE for more details.

* An error message appears saying 'Could not configure linear access'.

    The optimal video configuration could not be set up on your machine.
    ToonStruck requires either UniVBE correctly installed or VESA 2.0
    driver support from your video card manufacturer. See the section on
    UniVBE or Contact your video card manufacturer for details on
    obtaining a VESA 2.0 driver for your specific video card.

* The screen flickers heavily and the image appears split and does not appear
  centered on the screen.

    Attempt to run the game with single-buffered video using the command
    line: TOONSTRK -B.

    Note: This switch is required for the ATI 3D Rage/ATI 3D Xpression PCI 
    (commonly found in the SONY VAIO series) if running without Univbe.

* An error message appears saying 'Out of memory'.

    We recommend playing the game in the default screen setting on any 8
    Megabyte machine. First make sure that you have not modified the
    TOONSTRK.CFG, if you have, rerun the SETUP program and reinstall the
    video card.

    If you still do not have enough memory to play ToonStruck, memory may be
    being used by other software or your memory is configured incorrectly.
    ToonStruck requires a minimum of 7Mb free. If you are running the 
    game from a Windows '95 DOS box (or prompt), restart in MS-DOS Mode if
    you have an 8Mb system, or, if you have more, try altering the memory
    allocation in the DOS session properties box by setting the 'DPMI'
    section under the 'Memory' tab to 8192. If your system is running
    using the memory manager 'EMM386.EXE' try adding the switch '/NOEMS'
    to the command line in CONFIG.SYS. If your system is using another
    memory manager, such as 'QEMM', try disabling the expanded memory
    option using the memory managers setup utility. If you still experience
    problems try remarking out any references to programs that are loaded
    from AUTOEXEC.BAT and CONFIG.SYS ( SMARTDRV, EMM386 etc.). Be sure not
    to remark out references to MSCDEX, MOUSE and any sound card related
    programs. More memory can be saved by altering values set in CONFIG.SYS,
    try setting FILES=20 and BUFFERS=3. Finally, if this still doesn't work,
    create a boot disk and try to start your machine with this.

* The movies sometimes become jerky
    On some machines ( mostly 486's or machines with double-speed CD-ROM's )
    you may see a drop in resolution or frame-rate while watching some of
    the movie sequences (flicks). If you see this, don't panic, it's just the
    game trying to keep the picture and sound in sync so that you can enjoy 
    the acting, musical score and animation in ToonStruck at its best. If
    the movies do drop to a different resolution ( low video mode ) you can
    always go into the options screen (f1) and set the 'Video Mode' switch 
    back to 'HI'.

* The movies play out really slowly ( one frame per second )
    Your sound card has not been installed correctly and the movie player is
    attempting to stream music, but failing. To confirm this, re-run SETUP.EXE
    and select 'No Digital Device' in the manual section of sound setup. If the
    movies now play at normal speed you can return to SETUP.EXE and attempt to
    install the correct parameters for your sound card manually. If you are
    running from Windows '95 we suggest running in MS-DOS MODE. Restart to MS-DOS
    MODE, reinstall and try again.

* Problems with the F1, F5 and F6 keys during gameplay
    Toonstruck utilizes the F1, F5 and F6 keys during gameplay which may
    conflict with Windows 95 user-assigned shortcut keys. If you are running
    from the Dos Box (Prompt) in Win95 and have assigned "F1, F5 or F6" as
    shortcut keys, we suggest disabling them to run the game properly.


NOTE:  If you are running ToonStruck using an 'AST Advantage Adventure'
       series PC you may experience poor game performance and even system
       crashes. We have encountered problems using this series of machine.
       The CD-ROM Controller does not meet the minimum requirements for 
       Toonstruck, so you may want to try a different (new) disk controller
       card. If you do experience difficulties please contact AST for more
       information.

       If you have a zip drive by Iomaga installed on your PC, you may have
       problems with the installation routine. By inserting a disk into the zip
       drive, before installing ToonStruck, these problems seem to be bypassed.

------------------------------------------------------------------------------

                          Gameplay Instructions
                          ---------------------

Please read the manual for full instructions on how to play Toonstruck

Cursor Controls
---------------

* When cursor is a diagonal arrow pointer:
    Left or right click to move Drew to that point in the scene

* When cursor is a pointing hand (over exits, paths, doors etc.):
    Left click to walk towards exit and leave scene, right click to leave scene
    immediately

* When cursor is a magnifying glass:
    Left or right click to get (where appropriate) a description of whatever
    the cursor is over.

* When cursor is an opening and closing hand:
    Left click to 'use', & right click to get (where appropriate) a description
    of, whatever the cursor is over (you'll hear a silly noise if there is no
    description available).

* When cursor is chattering teeth:
    Left click to talk to, & right click to get a description of, the character
    the cursor is over. 

* When cursor is a 'picking up' hand:
    Left click to pick up (cursor turns into that object), & right click to get
    (where appropriate) a description of, whatever the cursor is over (you'll
    hear a silly noise if there is no description available). 


Using Objects
-------------

Having picked up an object, left click to 'use' that object in the current
scene (must be over the area of the scene where you want to use the object).
Alternatively, move the cursor over the inventory bag (see below) and left
click to place the object in your inventory (short cut: while the cursor is an
object, right click at any time to instantly place object in inventory bag).


Storing Objects
---------------

Bottom left of the screen is a small blue bag. Left or right click on the bag
to bring up a close-up of its contents. This close-up serves as the inventory
screen where useful objects may be stored for future use. Right click over any
object in the inventory screen to get a description of that object. Left click
on an object to pick it up, the cursor will become that object. Left click
over an empty slot to return the object to the bag. Whilst holding an object
left click away from another item or slot to return to the main scene still
'carrying' the object (as the cursor).


Flux Wildly
-----------

Flux is the purple guy following you around the game. Left click on Flux to
turn the cursor into a 'Flux Head'. In some places you can left click the Flux
Head cursor to "use" Flux or trigger additional dialog. Left click over Flux or
right click anywhere to return to normal cursor.


Other controls
--------------

Press F1 to bring up the Options screen.

Press F5 to bring up the Save Game screen.

Press F6 to bring up the Load Game screen.

Press 'spacebar' or 'esc' to 'fast forward' past the current line of dialog.
 
------------------------------------------------------------------------------

UniVBE and Uvconfig are copyright SciTech Software. All rights reserved.
Windows '95, MS-DOS and EMM386 are copyright Microsoft. All rights reserved. 
QEMM is copyright Quarterdeck. All rights reserved.
 
Release Notes : 1.1 : 10/18/96 @ 11:50
