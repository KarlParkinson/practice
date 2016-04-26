require_relative 'queue.rb'

class Stack

  def initialize
    @items = []
  end

  def push(i)
    @items << i
  end

  def pop
    return @items.pop
  end

  def peek
    return @items.last
  end

  def is_empty?
    return @items.empty?
  end

end

class MinStack < Stack

  def initialize
    super()
    @minVal = nil
  end

  def push(i)
    if (@minVal == nil || i < @minVal)
      @minVal = i
    end
    @items << i
  end

  def pop
    i = @items.pop
    if (i == @minVal)
      @minVal = @items.min
    end
    return i
  end

  def getMinimum
    return @minVal
  end

  def is_empty?
    return @items.empty?
  end

end

class MinStack2

  def initialize
    @items = []
    @min_stack = Stack.new
  end

  def push(i)
    if (@items.empty?)
      @min_stack.push(i)
      @items << i
    elsif (i < @min_stack.peek)
      @items << i
      @min_stack.push(i)
    else
      @items << i
      @min_stack.push(@min_stack.peek())
    end
  end

  def pop
    @min_stack.pop
    return @items.pop
  end

  def peek
    return @items.last
  end

  def getMinimum
    return @min_stack.peek
  end

  
end

class QueueStack

  def initialize
    @q1 = Queue.new
    @q2 = Queue.new
  end

  def push(i)
    @q1.enqueue(i)
  end

  def pop
    while (@q1.size > 1)
      @q2.enqueue(@q1.dequeue)
    end
    i = @q1.dequeue
    while (!@q2.is_empty?)
      @q1.enqueue(@q2.dequeue)
    end
    return i
  end

end

class QueueStack2

  def initialize
    @q1 = Queue.new
    @q2 = Queue.new
  end

  def pop
    return @q2.dequeue
  end

  def push(i)
    @q1.enqueue(i)
    while(!@q2.is_empty?)
      @q1.enqueue(@q2.dequeue)
    end
    while(!@q1.is_empty?)
      @q2.enqueue(@q1.dequeue)
    end
  end

end


#begin
  #s = MinStack2.new
  #s.push(5)
  #s.push(9)
  #s.push(3)
  #puts s.getMinimum
  #s.pop
  #puts s.getMinimum
  #s.pop
  #puts s.getMinimum
  #s.pop
  #puts s.getMinimum
#end
