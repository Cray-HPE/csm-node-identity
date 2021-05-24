# csm-node-identity

csm-node-identity is a systemd service which does the following:

1. Parses `/proc/cmdline` for `nid=` and `xname=` parameters, and
2. Creates the files `/etc/cray/nid` and `/etc/cray/xname`, as appropriate.

These files are required by other packages to determine node name information.

## Installation

csm-node-identity is installed via RPM using your OS-specific package manager.

## Usage

N/A

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Use [SemVer](https://semver.org) for versioning. The version must be updated as appropriate for the change in the `.version` file for all changes.

## License

MIT. See the `LICENSE` file.

## History

In Shasta 1.5 and previous releases of CSM `<1.2.0`, this package was provided by the HPE Cray Operating System (COS). The latest version was `0.4.5`.

## Changelog

- `1.0.0` - initial release included in the CSM product.

