require_relative 'queue.rb'
require_relative 'stack.rb'

qs = QueueStack2.new
qs.push(1)
qs.push(2)
qs.push(8)
qs.push("k")
puts qs.pop
puts qs.pop
