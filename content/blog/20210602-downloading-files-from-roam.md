---
title: "Downloading files uploaded to Roam Research for use with Obsidian"
date: 2021-06-01T23:27:59+02:00
draft: false
tags: ['text', 'english', 'python', 'roam research', 'obsidian', 'taking notes', 'zettelkasten']
---

If you've recently transitioned from [Roam Research](https://roamresearch.com) to [Obsidian](https://obsidian.md), you might run into a few issues, even after you've run the "Markdown format importer" core plugin. One of the most annoying ones that I ran into was that files uploaded to Roam (images, pdfs, etc.) are automatically uploaded to [Google Firebase](https://firebase.google.com/).

Roam assets are linked to in the Markdown files like this:

```markdown
![](https://firebasestorage.googleapis.com/v0/b/firescript-471a1.appspot.com/o/imgs%2Fapp%2FMyNotes%2FxRFXx7l-ZK.png?alt=media&token=1e03b680-5472-33dc-9b06-a127301af37f)
```

Now, since Roam relies on security by obscurity on this front, the links to your assets will still be accessible in your Obsidian vault, and they'll still render correctly. However, I still think it's worth downloading the files for three reasons:
- If you don't intend to use Roam anymore and cancel your subscription, they will likely delete those assets at some point, leaving you with a lot of broken links in Obsidian.
- Part of Obsidian's appeal is that you own your assets. Not so if they're on someone else's server.
- You can't access Firebase files without an internet connection.

So, instead, you want to download the contents of that link and replace it in your notes with something like this:

```markdown
![](assets/newfile.png)
```

That way, you'll have full control over all your assets, and you won't be dependent on those assets being stored on Firebase by Roam.

To fix this, I wrote a Python script that will:
- Go through every file and every folder within a specified root vault directory
- Look for links to Google Firebase
- Download all assets from Firebase to a local folder (`/assets` by default), using the timestamp and index number as a filename
- Replace the Firebase links in your vault with links to the newly downloaded files, accounting for PDFs, whose links are formatted differently in Roam as `{{ pdf: ... }}`

Before you run this script, I highly recommend backing up your vault or trying this out on a dummy vault.

{{< rawhtml >}}
<script src="https://gist.github.com/nicolevanderhoeven/b25c97a8a68ea97e7bdf5ee674fdaec4.js"></script>
{{< /rawhtml >}}

After downloading and saving the script, run `python3 downloadfirebase.py` on your terminal.

This worked really well for me, and I can breathe a little more easily now that my vault is self-contained.