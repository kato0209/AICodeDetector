

$ tail -n +1 MakeFile.java ReadDir.java 
==> MakeFile.java <==
import java.io.File;
import java.util.Arrays;

class MakeFile {
  public static void main(String[] args) throws Exception {
    File baseDir = new File(System.getProperty("java.io.tmpdir"));
    @SuppressWarnings("GoodTime") 
    String baseName = System.currentTimeMillis() + "-";

    for (int counter = 0; counter < 10000; counter++) {
      File tempDir = new File(baseDir, baseName + counter);
      if (tempDir.mkdir()) {
        System.out.println("created " + tempDir);
        System.out.print("press enter to continue");
        System.console().readLine();

        
        
        if (!tempDir.setReadable(false,  false)
            || !tempDir.setWritable(false,  false)
            || !tempDir.setExecutable(false,  false)
            
            || !tempDir.setReadable(true,  true)
            || !tempDir.setWritable(true,  true)
            || !tempDir.setExecutable(true,  true)) {
          throw new IllegalStateException(
              "Failed to ensure that " + tempDir + " has the expected ownership and permissions");
        }
        
        
        
        String[] children = tempDir.list();
        if (children == null || children.length != 0) {
          throw new IllegalStateException(
              "Failed to verify that " + tempDir + " is empty: " + Arrays.toString(children));
        }
        new File(tempDir, "one").createNewFile();
        new File(tempDir, "two").createNewFile();
        new File(tempDir, "three").createNewFile();
        return;
      }
    }
    throw new RuntimeException("could not create");
  }
}

==> ReadDir.java <==
import static java.nio.file.LinkOption.NOFOLLOW_LINKS;
import static java.util.Objects.requireNonNull;

import java.io.IOException;
import java.nio.file.DirectoryIteratorException;
import java.nio.file.DirectoryStream;
import java.nio.file.FileSystemException;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.SecureDirectoryStream;
import java.nio.file.attribute.BasicFileAttributeView;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

class ReadDir {
  public static void main(String[] args) throws Exception {
    deleteDirectoryContents(Path.of(args[0]));
  }

  public static void deleteDirectoryContents(Path path) throws IOException {
    Collection<IOException> exceptions = null; 
    try (DirectoryStream<Path> stream = Files.newDirectoryStream(path)) {
      if (stream instanceof SecureDirectoryStream) {
        SecureDirectoryStream<Path> sds = (SecureDirectoryStream<Path>) stream;
        exceptions = deleteDirectoryContentsSecure(sds);
      } else {
        throw new RuntimeException();
      }
    } catch (IOException e) {
      if (exceptions == null) {
        throw e;
      } else {
        exceptions.add(e);
      }
    }

    if (exceptions != null) {
      throwDeleteFailed(path, exceptions);
    }
  }

  
  private static Collection<IOException> deleteRecursivelySecure(
      SecureDirectoryStream<Path> dir, Path path) {
    Collection<IOException> exceptions = null;
    try {
      if (isDirectory(dir, path, NOFOLLOW_LINKS)) {
        try (SecureDirectoryStream<Path> childDir = dir.newDirectoryStream(path, NOFOLLOW_LINKS)) {
          exceptions = deleteDirectoryContentsSecure(childDir);
        }

        
        
        if (exceptions == null) {
          dir.deleteDirectory(path);
        }
      } else {
        dir.deleteFile(path);
      }

      return exceptions;
    } catch (IOException e) {
      return addException(exceptions, e);
    }
  }

  
  private static Collection<IOException> deleteDirectoryContentsSecure(
      SecureDirectoryStream<Path> dir) {
    Collection<IOException> exceptions = null;
    try {
      Iterator<Path> itr = dir.iterator();
      System.out.print("press enter to continue");
      System.console().readLine();
      while (itr.hasNext()) {
        Path path = itr.next();
        System.out.println(path);
      }

      return exceptions;
    } catch (DirectoryIteratorException e) {
      return addException(exceptions, e.getCause());
    }
  }

  
  private static boolean isDirectory(
      SecureDirectoryStream<Path> dir, Path name, LinkOption... options) throws IOException {
    return dir.getFileAttributeView(name, BasicFileAttributeView.class, options)
        .readAttributes()
        .isDirectory();
  }

  
  private static Path getParentPath(Path path) {
    Path parent = path.getParent();

    
    if (parent != null) {
      
      
      
      
      
      return parent;
    }

    
    if (path.getNameCount() == 0) {
      
      
      
      
       For working dir paths ("" and "C:"), return null because:
         A) it's not specified that "" is the path to the working directory.
         B) if we're getting this path for recursive delete, it's typically not possible to
            delete the working dir with a relative path anyway, so it's ok to fail.
         C) if we're getting it for opening a new SecureDirectoryStream, there's no need to get
            the parent path anyway since we can safely open a DirectoryStream to the path without
            worrying about a symlink.
      return null;
    } else {
       "foo" (working dir)
      return path.getFileSystem().getPath(".");
    }
  }

  
  private static Collection<IOException> addException(
      Collection<IOException> exceptions, IOException e) {
    if (exceptions == null) {
      exceptions = new ArrayList<>();  don't need Set semantics
    }
    exceptions.add(e);
    return exceptions;
  }

  
  private static Collection<IOException> concat(
      Collection<IOException> exceptions, Collection<IOException> other) {
    if (exceptions == null) {
      return other;
    } else if (other != null) {
      exceptions.addAll(other);
    }
    return exceptions;
  }

  
  private static void throwDeleteFailed(Path path, Collection<IOException> exceptions)
      throws FileSystemException {
    NoSuchFileException pathNotFound = pathNotFound(path, exceptions);
    if (pathNotFound != null) {
      throw pathNotFound;
    }
     TODO(cgdecker): Should there be a custom exception type for this?
     Also, should we try to include the Path of each file we may have failed to delete rather
     than just the exceptions that occurred?
    FileSystemException deleteFailed =
        new FileSystemException(
            path.toString(),
            null,
            "failed to delete one or more files; see suppressed exceptions for details");
    for (IOException e : exceptions) {
      deleteFailed.addSuppressed(e);
    }
    throw deleteFailed;
  }

  private static NoSuchFileException pathNotFound(Path path, Collection<IOException> exceptions) {
    if (exceptions.size() != 1) {
      return null;
    }
    IOException exception = exceptions.iterator().next();
    if (!(exception instanceof NoSuchFileException)) {
      return null;
    }
    NoSuchFileException noSuchFileException = (NoSuchFileException) exception;
    String exceptionFile = noSuchFileException.getFile();
    if (exceptionFile == null) {
      
      return null;
    }
    Path parentPath = getParentPath(path);
    if (parentPath == null) {
      
      return null;
    }
     requireNonNull is safe because paths have file names when they have parents.
    Path pathResolvedFromParent = parentPath.resolve(requireNonNull(path.getFileName()));
    if (exceptionFile.equals(pathResolvedFromParent.toString())) {
      return noSuchFileException;
    }
    return null;
  }
}


# In terminal #1:

$ javac MakeFile.java && sudo java MakeFile
created /tmp/1658849498447-0
press enter to continue

# In terminal #2:

$ javac ReadDir.java && java ReadDir /tmp/1658849498447-0
press enter to continue

Then press enter in terminal #1, which closes permissions.

Then press enter in terminal #2. It then successfully reads the directory that it would no longer have permissions to open:

/tmp/1658849498447-0/one
/tmp/1658849498447-0/three
/tmp/1658849498447-0/two

$ ls -l /tmp/1658849498447-0
ls: cannot open directory '/tmp/1658849498447-0': Permission denied
