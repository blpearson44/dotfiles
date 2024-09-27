# Ben Pearson's Dotfiles

## Chezmoi

I've recently switched from using stow to using [chezmoi](https://www.chezmoi.io/) to manage my dotfiles. I was finding myself having to use a number of work-arounds and custom scripting to support the separate machines I'm working on and manage external resources. My old dotfiles can be found in [blpearson44/dotfiles-stow](https://github.com/blpearson44/dotfiles-stow).

## Install

[Install chezmoi according to your system](https://www.chezmoi.io/install/) and then run the following command to download my dotfiles:

```bash
chezmoi init --apply blpearson44
```

To initialize it using ssh (my preferred authentication method) use
```bash
chezmoi init git@github.com:blpearson44/dotfiles.git
```

Alternatively you can run a one liner to install chezmoi and download my dotfiles. Note that this installation of chezmoi will not be managed by a package manager and will need to be manually updated.

```bash
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply blpearson44
```

Then, you can run `chezmoi apply` to apply my dotfiles to your system.

## Configuration

Check the [chezmoi quickstart guide](https://www.chezmoi.io/quick-start/) or `chezmoi --help` for instructions on how to add, edit, or otherwise configure dotfiles. Note that chezmoi will expose git commands for the repository through `chezmoi git` for your convenience

## TODO

I still have a number of steps to complete to finalize this setup. 
- [ ] [Manage machine-to-machine differences](https://www.chezmoi.io/user-guide/manage-machine-to-machine-differences/)
- [ ] [install packages declaratively](https://www.chezmoi.io/user-guide/advanced/install-packages-declaratively/)
