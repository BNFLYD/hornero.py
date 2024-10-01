use axum::{
  routing::get,
  Router,
};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
  let app = Router::new().route("/", get(|| async { "¡Hallo!" }));

  let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
  println!("Servidor escuchando en http://{}", addr);

  axum::Server::bind(&addr)
      .serve(app.into_make_service())
      .await
      .unwrap();
}