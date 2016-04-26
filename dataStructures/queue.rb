require_relative 'stack.rb'

class Queue

  def initialize
    @items = []
  end

  def enqueue(i)
    @items << i
  end

  def dequeue
    return @items.shift
  end

  def size
    return @items.length
  end

  def is_empty?
    return @items.empty?
  end

end

class StackQueue

  def initialize
    @inbox = Stack.new
    @outbox = Stack.new
  end

  def enqueue(i)
    if (@inbox.is_empty? and @outbox.is_empty?)
      @outbox.push(i)
    else
      @inbox.push(i)
    end
  end

  def dequeue
    i = @outbox.pop
    if (@outbox.is_empty?)
      while(!@inbox.is_empty?)
        @outbox.push(@inbox.pop)
      end
    end
    return i
  end

end

#begin
#  q = StackQueue.new
#  q.enqueue(1)
#  q.enqueue([3])
#  puts q.dequeue.to_s
#  puts q.dequeue.to_s
#end
