# Copyright (c) 2014 'Konstantin Makarchev'
# 
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

require 'json'

x = []

1000.times do
  h = {
    'x' => rand,
    'y' => rand,
    'z' => rand,
    'name' => ('a'..'z').to_a.shuffle[0..5].join + ' ' + rand(10000).to_s,
    'opts' => {'1' => [1, true]},
  }
  x << h
end

File.open("1.json", 'w') { |f| f.write JSON.pretty_generate('coordinates' => x, 'info' => "some info") }
