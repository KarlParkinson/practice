class HashTable

  def initialize
    @size = 17
    @keys = [nil]*@size
    @data = [nil]*@size
  end

  def put(key, data)
    hash_value = hash(key)
    if (@keys[hash_value].nil?)
      # no collision, found spot, insert new data
      @keys[hash_value] = key
      @data[hash_value] = data
    elsif (@keys[hash_value] == key)
      # no collision, found spot, replace old data
      @data[hash_value] = data
    else
      probe = 1
      hash_value = rehash(hash_value, probe)
      while (!@keys[hash_value].nil? and @keys[hash_value] != 'deleted' and @keys[hash_value] != key)
        probe += 1
        hash_value = rehash(hash_value, probe)
      end
      if (@keys[hash_value].nil? or @keys[hash_value] == 'deleted')
        # found open slot
        @keys[hash_value] = key
        @data[hash_value] = data
      elsif (@keys[hash_value] == key)
        # found spot, replace old data
        @data[hash_value] = data
      end
    end
  end

  def get(key)
    hash_value = hash(key)
    if (@keys[hash_value] == key)
      # found slot, return data
      return @data[hash_value]
    else
      probe = 1
      new_hash = rehash(hash_value, probe)
      while (@keys[new_hash] != key and !@keys[new_hash].nil? and new_hash != hash_value)
        probe += 1
        new_hash = rehash(new_hash, probe)
      end

      if (@keys[new_hash] == key)
        # found slot, return data
        return @data[new_hash]
      else
        # one of other two conditions, data not present
        return nil
      end
    end
  end

  def delete(key)
    hash_value = hash(key)
    if (@keys[hash_value] == key)
      # found slot, mark as delete, set data to nil
      @keys[hash_value] = 'deleted'
      @data[hash_value] = nil
    else
      probe = 1
      new_hash = rehash(hash_value, probe)
      while (@keys[new_hash] != key and !@keys[new_hash].nil? and new_hash != hash_value)
        probe += 1
        new_hash = rehash(new_hash, probe)
      end

      if (@keys[new_hash] == key)
        # found slot, mark as deleted, set data to nil
        @keys[new_hash] = 'deleted'
        @data[new_hash] = nil
      else
        # trying to delete value that does not exist
        return nil
      end
    end
  end

  def [](key)
    get(key)
  end

  def []=(key, data)
    put(key, data)
  end
      

  private

  def hash(key)
    return key % @size
  end

  def rehash(old, probe)
    return (old + probe**2) % @size
    #return (old+1) % @size
  end


end


begin
  h = HashTable.new
  (0..16).each do |i|
    h[i] = 'k'
  end
  h.delete(15)
  puts h.inspect
  puts ""
  h[15] = 'HELLO'
  puts ""
  puts h.inspect
end
