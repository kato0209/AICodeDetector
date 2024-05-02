import com.google.auto.value.AutoValue;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.TYPE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

/**
 * Marks an {@link plain AutoValue auto value} type as having Gson serialization.
 * <p>
 * This annotation is needed because the {@linkplain Retention retention} of {@code @AutoValue}
 * does not allow reflection at runtime.
 */
@Retention(RUNTIME)
@Target({TYPE})
@AutoValue
public @interface AutoGson {
}
