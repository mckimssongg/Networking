# Cisco Packet Tracer: Instalación en sistemas basados en Arch

### Créditos y Agradecimientos

Este documento incluye información y procedimientos recuperados de las contribuciones de Juan Pablo Yamamoto en GitHub, específicamente relacionados con la instalación de Cisco Packet Tracer en sistemas basados en Arch. La información detallada fue obtenida de:

- **Perfil de GitHub**: [Juan Pablo Yamamoto (jpyamamoto)](https://gist.github.com/jpyamamoto)
- **Guía específica**: [Instrucciones de instalación - Cisco Packet Tracer](https://gist.github.com/jpyamamoto/6fd4db9c11ac448c366f09a71f7b1cea)

Agradecemos a Juan Pablo Yamamoto por compartir sus conocimientos y recursos que han facilitado la elaboración de este documento. Para más detalles y actualizaciones, por favor, consulte directamente los enlaces proporcionados.

---



En la página oficial de descargas de Cisco, únicamente tenemos disponibles para su descarga las versiones para Windows, macOS y distribuciones de Linux basadas en Debian (archivo `.deb`).

Para distribuciones basadas en Arch (Arch Linux, Manjaro, EndeavourOS, etc) no tenemos una opción de descarga distribuida por Cisco, ni en los repositorios oficiales de Arch.

En el repositorio de usuarios [AUR](https://aur.archlinux.org/) tenemos disponible el paquete [packettracer](https://aur.archlinux.org/packages/packettracer), sin embargo, su instalación no puede ser efectuada por los métodos usuales: con un manejador de paquetes con acceso al AUR como `pamac`, `yay`, `pavu`, etc.

A continuación especifico las instrucciones que funcionaron en mi sistema (Manjaro kernel 5.15.91-1).

## Instrucciones

1. Clonar el contenido desde [packettracer en AUR](https://aur.archlinux.org/packages/packettracer). Elige el directorio que prefieras para realizar este procedimiento, al finalizar podrás eliminar los archivos de instalación. Por el resto del instructivo asumiré que los archivos fueron clonados en el directorio Home del usuario.

   ```bash
   git clone git clone https://aur.archlinux.org/packettracer
   ```
2. Descargar el archivo `.deb` provisto por Cisco desde la página de descargas oficiales: [https://skillsforall.com/resources/lab-downloads](https://skillsforall.com/resources/lab-downloads). Debes haber iniciado tu sesión de SkillsForAll antes de ingresar a la página.
3. Mover el archivo descargado al directorio clonado bajo el nombre `CiscoPacketTracer_820_Ubuntu_64bit.deb` o `CiscoPacketTracer_821_Ubuntu_64bit.deb` según la versión que hayas descargado.

   ```bash
   mv ~/Downloads/<nombre archivo>.deb ~/packettracer/CiscoPacketTracer_820_Ubuntu_64bit.deb
   ```
4. Construir e instalar el paquete. La bandera `s` instala las dependencias necesarias, y la bandera `i` instala Packet Tracer en el `PATH` del sistema operativo (específicamente en `/usr/bin/packettracer`). Es necesario tener el comando `makepkg` que viene de manera predeterminada en los sistemas Arch con manejador de paquetes `pacman`.

   ```bash
   makepkg -si
   ```
5. (Opcional) Eliminar los archivos de construcción.

   ```bash
   rm -rf ~/packettracer
   ```

El proceso anterior instala el programa Cisco Packet Tracer en el `PATH` del sistema, siendo posible iniciarlo con el comando `packettracer` desde una terminal. Además, genera un archivo `.desktop` que es detectado por los lanzadores de menú como los incluidos por defecto en Gnome, Plasma, xfce; o con otros como dmenu, rofi, etc.

## Recursos

Para más información:

- [PacketTracer en Arch Wiki](https://wiki.archlinux.org/title/PacketTracer)
- [PacketTracer en AUR](https://aur.archlinux.org/packages/packettracer)
