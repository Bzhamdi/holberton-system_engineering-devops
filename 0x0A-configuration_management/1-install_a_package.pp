# install puppet-lint
#ensure => What state the package should be in,you can choose which package to retrieve 
#by specifying a version number or latest as the ensure value
#provide => Installation from an "exmple" software directory
#Ruby Gem support.
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
