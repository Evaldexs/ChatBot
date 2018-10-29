# Chat-Bot
A project for our chat bot

IMPORTANT:
1. Use Python as your programming language and use DISCORD.py (rewrite version) as your library!

Installation: 

The rewrite is the next major version of discord.py.

It is a massive breaking change. You can think of it as an entirely new library.

Some helpful links:

- https://github.com/Rapptz/discord.py/tree/rewrite for the source code
- http://discordpy.readthedocs.io/en/rewrite/ for the documentation
- http://discordpy.readthedocs.io/en/rewrite/migrating.html for a migrating guide from async -> rewrite
- https://github.com/Rapptz/discord.py/tree/rewrite/examples for examples

If you are interested in beta testing the rewrite you can install it by doing the following (requires git):

Do not install this if you don't want to help test this out, either by reporting bugs or asking for improvements.

----------------------------------------------------------------------------------------------------------------------------------------------
$ python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
# or with voice
$ python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
---------------------------------------------------------------------------------------------------------------------------------------------

After installing the rewrite, please do ?sub rewrite in #deleted-channel so you can be up-to date on the latest development and breaking changes.

If you want to help test the rewrite, you must be willing to update. Not updating makes the beta testing aspect useless.

Please note that the API itself is not finalised. There are chances that an update might break your bot due to an error on my part. However, it is fairly usable. Until the rewrite is fully released I will make more breaking changes in the future to the API. However bug reports and feature requests are appreciated.
