package_sn = 'ness123'
engine_hours = 1987.654321
MAX_HOURS = 30000

# old school
s = 'Package %s has %.2f engine hours (%d%%)' % (package_sn, engine_hours, 100*engine_hours / MAX_HOURS)
print(s)

# format
# notice that int must be ther for :d to work
s = 'Package {} has {:.2f} engine hours ({:d}%)'.format(package_sn, engine_hours, int(100*engine_hours / MAX_HOURS))
print(s)

# named format
s = 'Package {package} has {hours:.2f} engine hours ({percent:d}%)'.format(
    package=package_sn, hours=engine_hours, percent=int(100*engine_hours / MAX_HOURS)
)
print(s)

# fstring
s = f'Package {package_sn} has {engine_hours:.2f} engine hours ({int(100*engine_hours / MAX_HOURS):d}%)'
print(s)
