import okhttp3.OkHttpClient
import okhttp3.Request

val client = OkHttpClient()

val request = Request.Builder()
    .url("http://localhost:3000")
    .build()

client.newCall(request).execute().use { response ->
    if (!response.isSuccessful) throw IOException("Unexpected code $response")

    println(response.body!!.string()) // "Hello, World!"
}
