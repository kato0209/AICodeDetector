import com.google.auto.value.AutoValue;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Main {
  public static void main(String... args) <extra_id_0>   Gson gson = new <extra_id_1>       .registerTypeAdapterFactory(new AutoValueAdapterFactory())
        .create();
    Test inTest = Test.of("John", "Doe", 100);
    System.out.println("IN: " + inTest);
  <extra_id_2> String <extra_id_3> gson.toJson(inTest);
    System.out.println("JSON: " + json);
    Test outTest = gson.fromJson(json, Test.class);
    System.out.println("OUT: " + outTest);
  }

  @AutoValue @AutoGson
  public abstract static <extra_id_4> {
    public <extra_id_5> of(String firstName, String lastName, int age) {
 <extra_id_6>    return <extra_id_7> lastName, age);
    }

 <extra_id_8>  public abstract