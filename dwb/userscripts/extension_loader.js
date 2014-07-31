#!javascript
//<youtube_html5___SCRIPT
extensions.load("youtube_html5", {
//<youtube_html5___CONFIG
  // Command for an external video player 
  externalPlayer : "mplayer %u",

  // Shortcut to launch the external player
  externalShortcut : "eym",

  // Shortcut for the external player
  externalQuality : "1080p",

  // Shortcut for toggling pause/play, 
  togglePlay    : "yp",

  // Seek to position, "37ys" will seek to 37% of the video, :yt_seek 3:55 will
  // seek to position 3:55 default: "ys"
  seek          : "ys",

  // Seek forward, e.g. 7yf will seek 7*seekStep forward, :yt_seek_forward 1:37
  // will seek forward 1 minute and 37 seconds default: "yf"
  seekForward   : "yf",

  // Seek backward, e.g. 7yb will seek 7*seekStep forward, :yt_seek_backward 1:37
  // will seek backward 1 minute and 37 seconds default: "yb"
  seekBackward  : "yb",

  // Seekstep in seconds
  seekStep      : 5,

  // Whether to automatically start the video, 
  autoplay : false, 

  // Whether to show controls, 
  controls : true,

  // The default quality, possible qualities are 1080p, 720p, 480p, 360p, 240p
  // If the quality isn't available the next lower quality will be chosen
  defaultQuality : "480p",

  // Array of qualities that should not be offered, 
  excludeQuality : [  ],
  
  // The preferred video format, possible formats are x-flv, webm, mp4, 3gpp If
  // the format isn't available the first available will be chosen.
  preferredFormat : "",

  // Array of formats that should be excluded
  excludeFormat : [ ],
  
  foregroundActive : "#008000",
  foregroundColor : "#fff", 
  backgroundColor : "#000", 
  linkColor : "#999", 

  backgroundDisabled : "#555", 
  foregroundDisabled : "#aaa", 
  separator : "",
  font : "10px helvetica",
  linkFont : "bold 10px helvetica",

  barHeight : 14
//>youtube_html5___CONFIG
});
//>youtube_html5___SCRIPT
//<userscripts___SCRIPT
/*<userscripts___DISABLED
extensions.load("userscripts", {
//<userscripts___CONFIG
  // paths to userscripts, this extension will also load all scripts in from 
  // $XDG_CONFIG_HOME/.config/dwb/scripts
  scripts : []
//>userscripts___CONFIG
});
userscripts___DISABLED>*/
//>userscripts___SCRIPT

//<adblock_subscriptions___SCRIPT
extensions.load("adblock_subscriptions", {
//<adblock_subscriptions___CONFIG
// To take effect dwb needs to be restarted

// Shortcut to subscribe to a filterlist
scSubscribe : null, 
// Command to subscribe to a filterlist
cmdSubscribe : "adblock_subscribe", 

// Shortcut to unsubscribe from a filterlist
scUnsubscribe : null, 

// Command to unsubscribe from a filterlist
cmdUnsubscribe : "adblock_unsubscribe",

// Path to the filterlist directory, will be created if it doesn't exist. 
filterListDir : data.configDir + "/adblock_lists"
//>adblock_subscriptions___CONFIG
});
//>adblock_subscriptions___SCRIPT
//<requestpolicy___SCRIPT
extensions.load("requestpolicy", {
//<requestpolicy___CONFIG
    // path to a whitelist 
    whiteList : data.configDir + "/" + data.profile + "/requestpolicy.json",

    // shortcut to block/allow requests
    shortcut : "erp",

    // shortcut to unblock requests from current site that are blocked on all
    // sites
    unblockCurrent : "erC",

    // shortcut to unblock requests that are blocked on all sites
    unblockAll : "erA",

    // reload current site after blocking / unblocking a request
    autoreload : true, 

    // notify about blocked requests
    notify : false

    //>requestpolicy___CONFIG
});
//>requestpolicy___SCRIPT
//<simplyread___SCRIPT
extensions.load("simplyread", {
//<simplyread___CONFIG
// Shortcut to toggle simplyread
shortcut : "SR", 

// Command to toggle simplyread
command : "simplyread",

// Whether to use a stylesheet
nostyle : false, 

// Whether to show links
nolinks : false 

//>simplyread___CONFIG
});
//>simplyread___SCRIPT
//<contenthandler___SCRIPT
extensions.load("contenthandler", {
//<contenthandler___CONFIG
  // %u will be replaced with the uri of the request
  
  // Handle requests based on filename extension
  extension : {
        "pdf" : "xterm -e 'wget -O ~/Downloads/Tmp.pdf %u && zathura ~/Downloads/Tmp.pdf && rm ~/Downloads/Tmp.pdf'"
  //  "torrent" : "xfce4-terminal -e 'deluge %u'", 
  //   "pdf" : "xterm -e 'wget %u --directory-prefix=~/mypdfs'"
  },

  // Handle requests based on URI scheme
  uriScheme : {
    //"magnet" : "deluge %u'
    // "ftp" : "xterm -e 'ncftp %u'"
  },

  // Handle requests based on MIME type
  mimeType : {
    // "application/pdf" : "xterm -e 'wget %u --directory-prefix=~/mypdfs'"
  }
//>contenthandler___CONFIG
});
//>contenthandler___SCRIPT
//<formfiller___SCRIPT
extensions.load("formfiller", {
//<formfiller___CONFIG
// shortcut that gets and saves formdata
scGetForm : "efg",

// shortcut that fills a form
scFillForm : "eff",

// path to the formdata file
formData : data.configDir + "/forms",

// whether to use a gpg-encrypted file
useGPG : false,

// your GPG key ID (leave empty to use a symmetric cipher)
GPGKeyID : "",

// whether to use a GPG agent (requires non-empty GPGKeyID to work)
GPGAgent : false,

// additional arguments passed to gpg2 when encrypting the formdata
GPGOptEncrypt : "",

// additional arguments passed to gpg2 when decrypting the formdata
GPGOptDecrypt : "",

// whether to save the password in memory when gpg is used
keepPassword : true,

// whether to save the whole formdata in memory when gpg is used
keepFormdata : false

//>formfiller___CONFIG
});
//>formfiller___SCRIPT
