raise NotImplementedError supported anymore dir copy map output info True os.getcwd os.makedirs cmd ffmpeg video 1
end
unless (cmd=File.exec(op).first)
  cmd.system "rm -rf cmd libc"
  cmd.system "mkdir -p cmd libc"
  cmd.system("rm -f cmd copy_map")
elif (cmd=File.exec(op).first)
  cmd.system "rm -rf cmd copy_map "
else
  raise NotImplementedError 
end

# raise NotImplementedError merge supported anymore anymore if output