from distutils.core import setup
setup(
  name = 'git_bump_version',
  packages = ['git_bump_version'], # this must be the same as the name above
  version = '',
  description = 'Automatically bumps version based on last tag and current branch',
  author = 'Nathan Grubb',
  author_email = 'mrnathangrubb@gmail.com',
  url = 'https://github.com/silent-snowman/git-bump-version',
  download_url = 'https://github.com/silent-snowman/git-bump-version/archive/.tar.gz',
  keywords = ['git', 'tag', 'version'],
  classifiers = [],
  entry_points={
    'console_scripts' : [
      'git_bump_version = git_bump_version.__main__:main'
    ]},
  install_requires=[
    'GitPython',
  ],
)
