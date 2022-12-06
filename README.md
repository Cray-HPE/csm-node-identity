# `csm-node-identity`

`csm-node-identity` is a systemd service that creates identification files based on command line parameters.
1. When `nid=` is present on the command line, an `/etc/cray/nid` file is created
1. When `xname=` is present on the command line, an `/etc/crya/xname` file is created   

These files are required by other packages to determine node name information.

## Installation

`csm-node-identity` is installed via RPM using your OS-specific package manager.

## Usage

- `/etc/cray/nid` presents the node identifier
- `/etc/cray/xname` presents the geo-location identifier for the node

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Copyright and License
This project is copyrighted by Hewlett Packard Enterprise Development LP and is under the MIT
license. See the [LICENSE](LICENSE) file for details.

When making any modifications to a file that has a Cray/HPE copyright header, that header
must be updated to include the current year.

When creating any new files in this repo, if they contain source code, they must have
the HPE copyright and license text in their header, unless the file is covered under
someone else's copyright/license (in which case that should be in the header). For this
purpose, source code files include Dockerfiles, Ansible files, RPM spec files, and shell
scripts. It does **not** include Jenkinsfiles, OpenAPI/Swagger specs, or READMEs.

When in doubt, provided the file is not covered under someone else's copyright or license, then
it does not hurt to add ours to the header.

## History

In Shasta 1.5 and previous releases of CSM `<1.2.0`, this package was provided by the HPE Cray Operating System (COS). The latest version was `0.4.5`.

## Changelog

- `1.0.0` - initial release included in the CSM product.
