import com.google.auto.value.AutoValue;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Main {
  public static void main(String... args) {   Gson gson = new GsonBuilder()       .registerTypeAdapterFactory(new AutoValueAdapterFactory())
        .create();
    Test inTest = Test.of("John", "Doe", 100);
    System.out.println("IN: " + inTest);
   String json = gson.toJson(inTest);
    System.out.println("JSON: " + json);
    Test outTest = gson.fromJson(json, Test.class);
    System.out.println("OUT: " + outTest);
  }

  @AutoValue @AutoGson
  public abstract static class Test {
    public static Test of(String firstName, String lastName, int age) {
     return new AutoValue_Main_Test(firstName, lastName, age);
    }

   public abstract