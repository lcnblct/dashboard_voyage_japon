#!/usr/bin/env python3
"""
Script pour redémarrer proprement l'application
"""

import subprocess
import time
import requests
import signal
import os

def stop_streamlit_processes():
    """Arrête tous les processus Streamlit"""
    
    print("🛑 Arrêt des processus Streamlit existants")
    print("=" * 50)
    
    try:
        # Recherche des processus Streamlit
        result = subprocess.run(
            ["ps", "aux"], 
            capture_output=True, 
            text=True
        )
        
        streamlit_processes = []
        lines = result.stdout.split('\n')
        for line in lines:
            if "streamlit" in line.lower() and "app.py" in line:
                parts = line.split()
                if len(parts) > 1:
                    pid = parts[1]
                    streamlit_processes.append(pid)
                    print(f"   Processus trouvé: PID {pid}")
        
        # Arrêt des processus
        for pid in streamlit_processes:
            try:
                os.kill(int(pid), signal.SIGTERM)
                print(f"   ✅ Processus {pid} arrêté")
            except Exception as e:
                print(f"   ❌ Erreur lors de l'arrêt du processus {pid}: {str(e)}")
        
        # Attente pour s'assurer que les processus sont arrêtés
        time.sleep(3)
        
        return len(streamlit_processes) > 0
        
    except Exception as e:
        print(f"❌ Erreur lors de la recherche des processus: {str(e)}")
        return False

def wait_for_port_available(port=8502, timeout=30):
    """Attend que le port soit disponible"""
    
    print(f"⏳ Attente que le port {port} soit disponible...")
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"http://localhost:{port}", timeout=2)
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print(f"✅ Port {port} disponible")
            return True
        except Exception:
            time.sleep(1)
    
    print(f"❌ Port {port} toujours utilisé après {timeout} secondes")
    return False

def start_streamlit_app():
    """Démarre l'application Streamlit"""
    
    print("\n🚀 Démarrage de l'application Streamlit")
    print("=" * 50)
    
    try:
        # Démarrage de Streamlit
        process = subprocess.Popen([
            "streamlit", "run", "app.py",
            "--server.port", "8502"
        ])
        
        print("⏳ Attente du démarrage...")
        time.sleep(5)
        
        # Vérification que l'application est accessible
        try:
            response = requests.get("http://localhost:8502", timeout=10)
            if response.status_code == 200:
                print("✅ Application démarrée avec succès")
                print(f"🌐 URL: http://localhost:8502")
                return process
            else:
                print(f"❌ Erreur HTTP: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Impossible d'accéder à l'application: {str(e)}")
            return None
            
    except Exception as e:
        print(f"❌ Erreur lors du démarrage: {str(e)}")
        return None

def main():
    """Fonction principale"""
    
    print("🔄 Redémarrage de l'application")
    print("=" * 60)
    
    # Arrêt des processus existants
    if stop_streamlit_processes():
        print("✅ Processus existants arrêtés")
    else:
        print("ℹ️  Aucun processus existant trouvé")
    
    # Attente que le port soit disponible
    if not wait_for_port_available():
        print("❌ Impossible de libérer le port 8502")
        print("\n🔧 Solutions manuelles:")
        print("1. Arrêtez manuellement l'application (Ctrl+C dans le terminal)")
        print("2. Redémarrez votre terminal")
        print("3. Utilisez un port différent: streamlit run app.py --server.port 8503")
        return False
    
    # Démarrage de la nouvelle instance
    process = start_streamlit_app()
    
    if process:
        print("\n🎉 Application redémarrée avec succès !")
        print("\n📋 Instructions:")
        print("1. Ouvrez http://localhost:8502 dans votre navigateur")
        print("2. Naviguez vers la page 'Assistant IA'")
        print("3. Testez l'assistant avec un message simple")
        print("4. Pour arrêter l'application, appuyez sur Ctrl+C")
        
        try:
            # Attendre que l'utilisateur arrête l'application
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Arrêt de l'application...")
            process.terminate()
            process.wait()
            print("✅ Application arrêtée")
    else:
        print("\n❌ Échec du redémarrage de l'application")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 