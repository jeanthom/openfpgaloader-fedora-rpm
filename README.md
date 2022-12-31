# openFPGALoader community RPMs

## Installing openFPGALoader on Fedora (and other RPM-based distributions)

```
sudo dnf copr enable mobicarte/openFPGALoader
sudo dnf install openFPGALoader
```

## Updating rpmspec and generating the RPM files from this repository

### Dependencies

```
sudo dnf install dnf-utils rpmdevtools rpmlint
```

### rpmspec linting

```
rpmlint openFPGALoader.spec
```

### Local build

```
spectool -g -R openFPGALoader.spec
rpmbuild -ba openFPGALoader.spec
```

